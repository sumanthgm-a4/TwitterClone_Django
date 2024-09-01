from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    usern = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.CharField(max_length=300)
    likes = models.ManyToManyField(User, related_name="post_likes")
    dislikes = models.ManyToManyField(User, related_name="post_dislikes")
    
    def __str__(self) -> str:
        return self.usern