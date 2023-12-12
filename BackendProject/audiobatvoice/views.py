from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Audio, AudioSegment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AudioSerializer, AudioSegmentSerializer, AudioSerializerPut
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def audio_list(request):
    audios = Audio.objects.all()
    serializer = AudioSerializer(audios, many=True)
    return JsonResponse(serializer.data, safe=False)


# @api_view(["GET"])
# def audio_detail(request, id):
#     audio = Audio.objects.get(pk=id)
#     audio_segments_children = []
#     if audio.get_audio_segment_children() is not None:
#         for object in audio.get_audio_segment_children():
#             object = AudioSegmentSerializer(object).data
#             audio_segments_children.append(object)
#     return JsonResponse(
#         {
#             "audio": AudioSerializer(audio).data,
#             "audio_segments_children": audio_segments_children,
#         }
#     )


# @api_view(["POST"])
# def audio_update(request, id):
#     audio = Audio.objects.get(pk=id)
#     audio_segments_children = []
#     for object in audio.get_audio_segment_children():
#         object = AudioSegmentSerializer(object).data
#         audio_segments_children.append(object)
#     return JsonResponse(
#         {
#             "audio": AudioSerializer(audio).data,
#             "audio_segments_children": audio_segments_children,
#         }
#     )


@api_view(["GET", "PUT"])
def audio_detail(request, id):
    try:
        audio = Audio.objects.get(pk=id)
    except audio.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    audio_segments_children = []
    if audio.get_audio_segment_children() is not None:
        for object in audio.get_audio_segment_children():
            object = AudioSegmentSerializer(object).data
            audio_segments_children.append(object)

    if request.method == "GET":
        serializer = AudioSerializer(audio)
        return Response(
            {"audio": serializer.data, "audio_segments": audio_segments_children}
        )

    elif request.method == "PUT":
        serializer = AudioSerializerPut(audio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"audio": serializer.data, "audio_segments": audio_segments_children}
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
