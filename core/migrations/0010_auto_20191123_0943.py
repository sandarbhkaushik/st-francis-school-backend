# Generated by Django 2.2.7 on 2019-11-23 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191123_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='core_page_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CorePage'),
        ),
    ]