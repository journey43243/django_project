# Generated by Django 5.0.4 on 2024-06-09 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_remove_product_maker_remove_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Maker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lending.companys'),
        ),
    ]