from django.contrib import admin
from .models import Notice, Requirement, Scholarship
from .models import Download

admin.site.register(Notice)
admin.site.register(Requirement)
admin.site.register(Scholarship)
@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):

    list_display = ("title","category","order","is_active")

    list_editable = ("order","is_active")

    search_fields = ("title",)