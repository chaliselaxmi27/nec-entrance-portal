from django.urls import path
from .views import program_detail_tabs

urlpatterns = [
    path("program-details/", program_detail_tabs, name="program_details_tabs"),
    path("program-details/<slug:slug>/", program_detail_tabs, name="program_details_tabs_slug"),
]