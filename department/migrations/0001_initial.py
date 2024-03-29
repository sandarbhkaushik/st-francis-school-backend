# Generated by Django 2.2.5 on 2019-11-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
    ]
