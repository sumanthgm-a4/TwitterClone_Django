from django.db import models

# Create your models here.

class Tweet(models.Model):
    usern = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return self.usern