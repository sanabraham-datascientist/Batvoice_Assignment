from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from accounts.views import login_view,register_view,logout_view

urlpatterns = [
    path('api/',include('audiobatvoice.urls')),
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
