# Generated by Django 3.0 on 2020-06-26 13:18

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20200625_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/audio/'), upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/images/'), upload_to='images'),
        ),
        migrations.AlterField(
            model_name='note',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/notes/'), upload_to='notes'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(default='/media/video/', storage=django.core.files.storage.FileSystemStorage(location='/media/video/'), upload_to='video'),
        ),
    ]