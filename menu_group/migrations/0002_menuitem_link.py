# Generated by Django 2.2.5 on 2019-11-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
