from django.urls import path
from .views import (
    audio_list_view,
    audio_user_list_view,
    # audio_create_view,
    audio_update_view,
    audio_detail_view,
)

app_name = "audios"
urlpatterns = [
    path("mylist", audio_user_list_view, name="list"),
    path("", audio_list_view, name="list"),
    # path("create/", audio_create_view, name="create"),
    path("<int:id>/edit/", audio_update_view, name="update"),
    path("<int:id>/", audio_detail_view, name="detail"),
]
