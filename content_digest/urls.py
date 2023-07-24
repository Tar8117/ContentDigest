from django.urls import path
from .views import DigestView


urlpatterns = [
    path('create_digest/<int:user_id>/', DigestView.as_view(), name='digest'),
]
