# Generated by Django 5.0.4 on 2024-06-09 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0004_users_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='adressToServe',
            new_name='adressToOrder',
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='usersOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderPositions', models.JSONField()),
                ('userLogin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lending.users')),
            ],
        ),
    ]