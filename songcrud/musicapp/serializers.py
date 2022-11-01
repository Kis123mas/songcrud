from rest_framework import serializers
from .models import Artiste, Song, Lyric


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'age'
        )
        model = Artiste


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'artiste',
            'title',
            'date_released',
            'likes',
            'artiste_Id'
        )
        model = Song


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'song',
            'content',
            'song_Id'
        )
        model = Lyric