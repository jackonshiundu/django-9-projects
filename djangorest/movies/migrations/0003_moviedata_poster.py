# Generated by Django 5.1 on 2024-09-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_gener'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='poster',
            field=models.ImageField(default='media/None/Noimg.jpg', upload_to='media/'),
        ),
    ]
