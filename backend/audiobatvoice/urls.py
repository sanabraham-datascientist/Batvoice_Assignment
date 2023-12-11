from django.urls import path
from .views import audio_list, audio_detail

app_name = "audios"
urlpatterns = [
    path("", audio_list, name="list"),
    path("<int:id>/", audio_detail, name="detail"),
    # path("mylist", AudioUserListView.as_view(), name="mylist"),
    # path("<int:id>/edit/", AudioDetailView.as_view(), name="update"),
]
