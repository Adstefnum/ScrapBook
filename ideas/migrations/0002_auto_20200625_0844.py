# Generated by Django 3.0 on 2020-06-25 07:44

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file_cat_name',
        ),
        migrations.AddField(
            model_name='files',
            name='cat_name',
            field=models.CharField(choices=[('videos', 'VIDEOS'), ('audios', 'AUDIOS'), ('notes', 'NOTES'), ('images', 'IMAGES')], default='notes', max_length=8),
        ),
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(default='/media/files/git.txt', storage=django.core.files.storage.FileSystemStorage(location='/media/files/'), upload_to='files'),
        ),
        migrations.AddField(
            model_name='files',
            name='sub_cat',
            field=models.CharField(default='tech', max_length=100),
        ),
        migrations.AlterField(
            model_name='files',
            name='file_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
