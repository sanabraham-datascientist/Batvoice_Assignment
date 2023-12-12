from rest_framework import serializers
from .models import Audio, AudioSegment


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = (
            "id",
            "title",
            "length",
            "audio_file",
            "customer",
            "status",
            "anatator",
            "description",
            "get_absolute_url",
            "get_edit_url",
            "user_name",
            #"updated_at_formatted",
            "timestamp",
        )


class AudioSerializerPut(serializers.ModelSerializer):
    model = Audio
    fields = ("id", "audio_file", "transcript", "status")


class AudioSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioSegment
        fields = (
            "id",
            "audio_file",
            "length",
            "transcript",
        )
