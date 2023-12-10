from django.shortcuts import render, get_object_or_404, redirect
from .models import Audio, AudioSegment
from .forms import AudioForm, AudioSegmentForm
from django.forms.models import modelformset_factory


def audio_list_view(request):
    query_set = Audio.objects.all()
    context = {"object_list": query_set}
    return render(request, "audiobatvoice/list.html", context)


def audio_user_list_view(request):
    query_set = Audio.objects.filter(anatator=request.user)
    context = {"object_list": query_set}
    return render(request, "audiobatvoice/my_list.html", context)


def audio_detail_view(request, id=None):
    obj = get_object_or_404(Audio, pk=id)
    context = {"object": obj}
    return render(request, "audiobatvoice/detail.html", context)



def audio_update_view(request, id=None):

    obj = get_object_or_404(Audio, pk=id, anatator=request.user)
    form = AudioForm(request.POST or None, instance=obj)
    AudioSegmentFormset = modelformset_factory(AudioSegment, form=AudioSegmentForm, extra=0)
    query_set = obj.audiosegment_set.all()
    formset = AudioSegmentFormset(request.POST or None , queryset=query_set)
    context = {
        "form": form, "object": obj,"formset":formset
        }
    if all([form.is_valid(),formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            if child.audio is None:
                print("Added New")
                child.audio = parent
            child.save()
        context["message"] = "saved data"
    return render(request, "audiobatvoice/update.html", context)
