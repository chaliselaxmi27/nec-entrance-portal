from django.urls import path
from .views import program_detail

urlpatterns = [
    path('programs/<slug:slug>/', program_detail, name='program_detail'),
]