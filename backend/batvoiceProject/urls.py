from django.contrib import admin
from django.urls import path,include
from accounts.views import login_view,register_view,logout_view
from audiobatvoice.views import audio_list_view

urlpatterns = [
    path('audios/',include('audiobatvoice.urls')),
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
]
