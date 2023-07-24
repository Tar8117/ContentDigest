from django.contrib import admin
from .models import User, Subscription, Post, Digest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'source_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription', 'content', 'popularity')


@admin.register(Digest)
class DigestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_post_titles')

    def get_post_titles(self, obj):
        return ", ".join([post.content for post in obj.posts.all()])

    get_post_titles.short_description = 'Posts'
