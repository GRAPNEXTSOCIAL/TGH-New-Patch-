# Generated by Django 4.0.4 on 2022-12-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_itemgroup_item_group_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]