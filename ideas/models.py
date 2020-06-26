from django.db import models
from django.core.files.storage import FileSystemStorage

CAT_CHOICES = (
    ('tech','TECH'),
    ('class_mus','CLASSICAL MUSIC'),
    ('gen','GENERAL'),
    ('gen_music','GENERAL MUSIC'),
    ('novels','NOVELS'),
    ('physics','PHYSICS'),
    ('maths','MATHS'),
)

class Video(models.Model):
	file_pic = models.FileField(storage=FileSystemStorage(location='/media/image/'),upload_to='image',default='/media/image/')
	cat_name = models.CharField(max_length=30, choices=CAT_CHOICES, default='notes')
	file_name = models.CharField(max_length=100)
	file = models.FileField(storage=FileSystemStorage(location='/media/video/'),upload_to='video',default='/media/video/')
	last_date = models.DateField()
	

	def __str__(self):
		return self.file_name 

class Audio(models.Model):
	file_pic = models.FileField(storage=FileSystemStorage(location='/media/image/'),upload_to='image',default='/media/image/')
	cat_name = models.CharField(max_length=30, choices=CAT_CHOICES, default='notes')
	file_name = models.CharField(max_length=100)
	file = models.FileField(storage=FileSystemStorage(location='/media/audio/'),upload_to='audio')
	last_date = models.DateField()
	

	def __str__(self):
		return self.file_name 

class Image(models.Model):
	file_pic = models.FileField(storage=FileSystemStorage(location='/media/image/'),upload_to='image',default='/media/image/')
	cat_name = models.CharField(max_length=30, choices=CAT_CHOICES, default='notes')
	file_name = models.CharField(max_length=100)
	file = models.FileField(storage=FileSystemStorage(location='/media/images/'),upload_to='images')
	last_date = models.DateField()
	

	def __str__(self):
		return self.file_name 

class Note(models.Model):
	file_pic = models.FileField(storage=FileSystemStorage(location='/media/image/'),upload_to='image',default='/media/image/')
	cat_name = models.CharField(max_length=30, choices=CAT_CHOICES, default='notes')
	file_name = models.CharField(max_length=100)
	file = models.FileField(storage=FileSystemStorage(location='/media/notes/'),upload_to='notes')
	last_date = models.DateField()
	

	def __str__(self):
		return self.file_name 