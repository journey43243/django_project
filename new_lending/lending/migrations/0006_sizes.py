# Generated by Django 5.0.4 on 2024-07-28 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0005_usersorders_order_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lending.product')),
            ],
        ),
    ]
