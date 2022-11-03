from django.db import models
from datetime import datetime


#Creating (3)models Artiste, Song and Lyrics here.
class Artiste(models.Model):
    # class attribute for artiste
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()


    def __str__(self):
        return str(self.first_name)    #specifing string method

    

class Song(models.Model):
    # class attribute for song
    artiste_id = models.ForeignKey("Artiste", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    

    def __str__(self):
        return str(self.title) #specifing string method


class Lyric(models.Model):
    #attribute for lyrics
    song_id = models.ForeignKey("Song", on_delete=models.CASCADE)
    content = models.TextField() 

    def __str__(self):
        return str(self.song_id)    #specifing string method
    