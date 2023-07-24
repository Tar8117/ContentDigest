from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return self.source_name


class Post(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    content = models.TextField()
    popularity = models.IntegerField()

    def __str__(self):
        return f'{self.content}. {self.popularity}'


class Digest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.user} - {self.posts}'
