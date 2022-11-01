"""songcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import ListArtiste, DetailArtiste, ListSong, DetailSong, ListLyric, DetailLyric

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),

    path('artiste', ListArtiste.as_view(), name='artiste'),
    path('artiste/<int:pk>/', DetailArtiste.as_view(), name=''),

    path('song', ListSong.as_view(), name='song'),
    path('song/<int:pk>/', DetailSong.as_view(), name=''),

    path('lyric', ListLyric.as_view(), name='lyric'),
    path('lyric/<int:pk>/', DetailLyric.as_view(), name=''),
]
