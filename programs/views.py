from django.shortcuts import render, get_object_or_404
from .models import Program, ProgramDetail
from core.models import SiteSetting

def program_detail_tabs(request, slug=None):
    programs = Program.objects.filter(is_active=True).order_by("display_order", "name")

    if slug:
        active_program = get_object_or_404(Program, slug=slug, is_active=True)
    else:
        active_program = programs.first()

    active_detail = None
    if active_program:
        active_detail = ProgramDetail.objects.filter(
            program=active_program,
            is_active=True
        ).first()

    context = {
        "site": SiteSetting.objects.first(),
        "programs": programs,
        "active_program": active_program,
        "active_detail": active_detail,
    }
    return render(request, "programs/program_detail_tabs.html", context)