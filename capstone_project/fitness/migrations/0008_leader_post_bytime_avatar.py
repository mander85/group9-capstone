# Generated by Django 4.1 on 2022-11-16 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0007_alter_generator_exercises_exercise_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader_post_bytime',
            name='avatar',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
