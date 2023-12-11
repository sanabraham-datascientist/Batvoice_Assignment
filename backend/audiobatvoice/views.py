from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Audio, AudioSegment
from .forms import AudioForm, AudioSegmentForm
from django.forms.models import modelformset_factory
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AudioSerializer, AudioSegmentSerializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST


@api_view(["GET"])
def audio_list(request):
    audios = Audio.objects.all()
    serializer = AudioSerializer(audios, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def audio_detail(request, id):
    audio = Audio.objects.get(pk=id)
    audio_segments_children = []
    for object in audio.get_audio_segment_children():
        object = AudioSegmentSerializer(object).data
        audio_segments_children.append(object)
    return JsonResponse(
        {
            "audio": AudioSerializer(audio).data,
            "audio_segments_children": audio_segments_children,
        }
    )

