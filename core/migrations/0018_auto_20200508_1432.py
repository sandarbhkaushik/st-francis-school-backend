# Generated by Django 2.2 on 2020-05-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_media_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='content',
            field=models.TextField(blank=True, max_length=2500),
        ),
    ]
