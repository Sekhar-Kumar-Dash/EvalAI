# Generated by Django 2.2.20 on 2023-10-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0106_challenge_worker_image_url_alter"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaderboarddata",
            name="is_disabled",
            field=models.BooleanField(default=False),
        ),
    ]
