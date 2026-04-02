from django.urls import path

from .views import notice_list, notice_detail

urlpatterns = [
    path('notices/', notice_list, name='notice_list'),
    path('notices/<slug:slug>/', notice_detail, name='notice_detail'),
    
]