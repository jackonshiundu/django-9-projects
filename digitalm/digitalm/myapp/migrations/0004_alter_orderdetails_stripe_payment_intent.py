# Generated by Django 5.1.1 on 2024-09-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_orderdetails_stripe_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='stripe_payment_intent',
            field=models.CharField(max_length=255),
        ),
    ]
