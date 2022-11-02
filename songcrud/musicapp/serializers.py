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
            'artiste_id',
            'title',
            'date_released',
            'likes',
        )
        model = Song


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'song_id',
            'content',
        )
        model = Lyric