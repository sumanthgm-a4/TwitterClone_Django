# Generated by Django 5.0.7 on 2024-09-01 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_tweet_likes"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="dislikes",
            field=models.ManyToManyField(
                related_name="post_dislikes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
