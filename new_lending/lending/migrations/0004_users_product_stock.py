# Generated by Django 5.0.4 on 2024-06-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0003_product_maker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32)),
                ('surname', models.CharField(blank=True, max_length=32)),
                ('login', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=32)),
                ('adressToServe', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(choices=[(1, 'In stock'), (0, 'Our stock')], default=1),
            preserve_default=False,
        ),
    ]