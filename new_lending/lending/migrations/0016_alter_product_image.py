# Generated by Django 5.0.4 on 2024-06-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0015_alter_product_descripton_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
