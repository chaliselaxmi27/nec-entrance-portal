from django.urls import path

from admission import views
from .views import downloads, home

urlpatterns = [
    path('', home, name='home'),
     path("downloads/", downloads, name="downloads"),

]