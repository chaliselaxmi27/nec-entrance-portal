from django.contrib import admin
from .models import Program, ProgramDetail


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order", "is_active")
    list_editable = ("display_order", "is_active")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProgramDetail)
class ProgramDetailAdmin(admin.ModelAdmin):
    list_display = ("program", "page_title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("page_title", "program__name")