from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Digest, Subscription, Post
from .serializers import DigestSerializer


class DigestView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            # логика по формированию дайджеста
            # выбираем все посты из источников, на которые подписан
            # пользователь и у которых популярность выше 50 (к примеру)
            subscriptions = Subscription.objects.filter(user=user)
            posts = Post.objects.filter(
                subscription__in=subscriptions, popularity__gt=50
            )
            if not posts.exists():
                return Response(
                    {'message': 'Недостаточно данных для формирования '
                                'дайджеста.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            digest = Digest.objects.create(user=user)
            digest.posts.set(posts)
            serializer = DigestSerializer(digest)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND
            )
