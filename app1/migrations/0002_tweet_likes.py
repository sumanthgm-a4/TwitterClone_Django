# Generated by Django 5.0.7 on 2024-09-01 11:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="likes",
            field=models.ManyToManyField(
                related_name="post_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
