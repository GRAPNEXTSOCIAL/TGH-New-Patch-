# Generated by Django 4.0.4 on 2022-12-12 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_product_color_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='color_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color_name',
        ),
    ]
