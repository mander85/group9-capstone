# Generated by Django 4.1 on 2022-09-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_delete_leader_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generator_Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.IntegerField()),
                ('exercise_name', models.CharField(max_length=120)),
                ('exercise_duration', models.IntegerField()),
            ],
        ),
    ]