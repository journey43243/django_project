# Generated by Django 5.0.4 on 2024-07-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0004_usersorders_order_name_usersorders_order_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersorders',
            name='order_place',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
