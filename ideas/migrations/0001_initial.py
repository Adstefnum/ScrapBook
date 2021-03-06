# Generated by Django 3.0 on 2020-06-25 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(choices=[('videos', 'VIDEOS'), ('audios', 'AUDIOS'), ('notes', 'NOTES'), ('images', 'IMAGES')], default='notes', max_length=8)),
                ('date_added', models.DateField()),
                ('cat_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=1000)),
                ('last_date', models.DateField()),
                ('file_cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.Category')),
            ],
        ),
    ]
