# Generated by Django 2.2 on 2020-05-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_group', '0003_auto_20200508_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
