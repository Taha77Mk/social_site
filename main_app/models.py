from django.db import models
from django.utils import timezone
from users.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # one user may have multiple post but one post have only one user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')  # delete user and his posts
    picture = models.ImageField(upload_to='media_cnd', blank=True, null=True)
    picture_2 = models.ImageField(upload_to='media_cnd', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class comments(models.Model):
    # user = models.ManyToManyField(Profile, on_delete=models.CASCADE, default=Profile,)
    guild = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})
