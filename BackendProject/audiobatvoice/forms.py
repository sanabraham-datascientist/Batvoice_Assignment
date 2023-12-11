from django import forms
from .models import Audio,AudioSegment


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ["audio_file"]


class AudioSegmentForm(forms.ModelForm):
    class Meta:
        model = AudioSegment
        fields = ["transcript"]
