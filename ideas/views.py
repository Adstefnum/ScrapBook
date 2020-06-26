from django.shortcuts import render
from django.views.generic import ListView
from .models import Video,Audio,Image,Note

class IndexView(ListView):
	template_name = "ideas/index.html"

	def get_queryset(self):
		return Note.objects.all()

class AudioView(ListView):
	template_name = "ideas/audio.html"

	def get_queryset(self):
		return Audio.objects.all()

class VideoView(ListView):
	template_name = "ideas/video.html"

	def get_queryset(self):
		return Video.objects.all()

class ImageView(ListView):
	template_name = "ideas/image.html"

	def get_queryset(self):
		return Image.objects.all()

class NoteView(ListView):
	template_name = "ideas/note.html"

	def get_queryset(self):
		return Note.objects.all()
