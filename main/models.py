from datetime import datetime

from django.db import models
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Текст')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, null=True)

    class Meta:
        unique_together = ['user', 'post']
