from django.contrib import admin
from .models import Download, PopupNotice, QuickLink
@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ("title","external_link", "category", "order", "is_active", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description", "external_link")
    list_editable = ("order", "is_active")
@admin.register(PopupNotice)
class PopupNoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "message")
    list_editable = ("is_active", "order")
@admin.register(QuickLink)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")