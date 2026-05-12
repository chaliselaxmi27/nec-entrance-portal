from django.urls import path
from .views import home, downloads

urlpatterns = [
    path("", home, name="home"),
    path("downloads/", downloads, name="downloads"),
    
]