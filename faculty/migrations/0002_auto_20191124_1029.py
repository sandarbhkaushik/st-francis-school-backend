# Generated by Django 2.2.7 on 2019-11-24 10:29

from django.db import migrations, models
import faculty.models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facultyprofile',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='facultyprofile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='facultyprofile',
            name='profile_image',
            field=models.FileField(blank=True, upload_to=faculty.models.get_file_path),
        ),
        migrations.AlterField(
            model_name='facultyprofile',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
