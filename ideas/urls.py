from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.IndexView.as_view(),name = "index"),
    path('index/',views.IndexView.as_view(),name = "index"),
    path('audio/',views.AudioView.as_view(),name = "audio"),
    path('video/',views.VideoView.as_view(),name = "video"),
    path('image/',views.ImageView.as_view(),name = "image"),
    path('note/',views.NoteView.as_view(),name = "note"),
]