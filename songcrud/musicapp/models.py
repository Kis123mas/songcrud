from django.db import models
from datetime import datetime


# Creating (3)models Artiste, Song and Lyrics here.
class Artiste(models.Model):
    # attribute for artiste
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()


class Song(models.Model):
    #attribute for song
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE) #An Artiste can have multiple songs and  song must only belong to one Artiste.
    date_released = models.DateField(default=datetime.today)
    likes = models.ManyToManyField()
    artiste_id =


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE) #song having multiple lyrics and a lyric must only belong to a song.
    #attribute for lyrics
    content = models.CharField(max_length=5000)

    song_id =
    
