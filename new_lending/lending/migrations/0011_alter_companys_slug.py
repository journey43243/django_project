# Generated by Django 5.0.4 on 2024-06-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0010_alter_companys_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companys',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
