from django.urls import path

from .views import notice_list, notice_detail
from admission import views

urlpatterns = [
    path('notices/', views.notice_list, name='notice_list'),
    path('notices/<slug:slug>/', views.notice_detail, name='notice_detail'),
    
]