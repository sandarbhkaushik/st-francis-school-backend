# Generated by Django 2.2 on 2020-05-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_auto_20191124_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyprofile',
            name='education',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
