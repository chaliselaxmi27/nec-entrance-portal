from django.contrib import admin
from .models import Download


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_active", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description")
    list_editable = ("order", "is_active")