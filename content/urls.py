
from django.urls import path, include
from .views import UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload', UploadFeed.as_view())
]



