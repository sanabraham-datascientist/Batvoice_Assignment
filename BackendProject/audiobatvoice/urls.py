from django.urls import path
from .views import audio_list, audio_detail

app_name = "audios"
urlpatterns = [
    path("", audio_list, name="list"),
    path("<int:id>/", audio_detail, name="detail"),
    path("<int:id>/edit/", audio_detail, name="update"),
]
