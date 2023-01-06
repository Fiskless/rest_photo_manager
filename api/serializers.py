from rest_framework import serializers

from api.models import Photo


class PhotoCreateSerializer(serializers.ModelSerializer):
    people_names = serializers.CharField(label='Имена людей на фото',
                                         max_length=255)

    class Meta:
        model = Photo
        fields = ["id", "photo", "geo_location", "description", "people_names"]


class PhotoWithoutMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "photo"]