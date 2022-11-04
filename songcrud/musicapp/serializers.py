from rest_framework import serializers
from .models import Artiste, Song

# serializers for models
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
