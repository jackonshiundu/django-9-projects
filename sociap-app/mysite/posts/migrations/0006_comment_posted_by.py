# Generated by Django 5.1 on 2024-08-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='echesajackon', max_length=100),
            preserve_default=False,
        ),
    ]
