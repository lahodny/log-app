# Generated by Django 3.1.14 on 2021-12-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20211116_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttype',
            name='icon',
            field=models.ImageField(default='', upload_to='icons/'),
        ),
    ]
