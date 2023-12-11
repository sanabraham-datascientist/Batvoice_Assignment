from rest_framework import serializers
from .models import Audio, AudioSegment


class AudioSerializer(serializers.ModelSerializer):
    # get_audio_segment_children = AudioSegmentSerializer()

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
            # "get_absolute_url",
            # "get_edit_url",
            # "get_audio_segment_children",
        )


class AudioSegmentSerializer(serializers.ModelSerializer):
    audio = AudioSerializer(read_only=True)

    class Meta:
        model = AudioSegment
        fields = (
            "id",
            "audio",
            "audio_file",
            "length",
            "transcript",
        )
