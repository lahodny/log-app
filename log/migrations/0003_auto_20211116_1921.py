# Generated by Django 3.1.13 on 2021-11-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_workout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='notes',
            field=models.TextField(blank=True, verbose_name='post workout notes'),
        ),
    ]