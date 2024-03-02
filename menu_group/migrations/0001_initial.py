# Generated by Django 2.2.5 on 2019-11-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Menu Item',
            },
        ),
    ]