# Generated by Django 4.0.4 on 2022-12-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_purchaseproduct_hsn_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemgroup',
            name='item_group_image',
            field=models.ImageField(upload_to='productimg'),
        ),
    ]
