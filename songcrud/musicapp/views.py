from django.http import HttpResponse
from rest_framework import generics
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello, This is my first web app.</h1>")


class ListArtiste(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class DetailArtiste(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class ListSong(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class DetailSong(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ListLyric(generics.ListCreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

class DetailLyric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
