from django.shortcuts import render
from core.models import SiteSetting, HeroSlide
from admission.models import Notice, Requirement, Scholarship
from programs.models import Program,ProgramDetail
from .models import Download,PopupNotice


def home(request):
    programs = Program.objects.filter(is_active=True).order_by("display_order", "name")

    slug = request.GET.get("program")

    if slug:
        active_program = Program.objects.filter(slug=slug).first()
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
        "hero_slides": HeroSlide.objects.filter(is_active=True).order_by("order"),
        "latest_notices": Notice.objects.all()[:10],
        "requirements": Requirement.objects.all(),
        "scholarships": Scholarship.objects.all(),
        "programs": Program.objects.filter(is_active=True).order_by("display_order"),
        "active_program": active_program,
        "active_detail": active_detail,
        "home_downloads": Download.objects.filter(is_active=True).order_by("order", "-created_at"),
        "active_popup": PopupNotice.objects.filter(is_active=True).order_by("order", "-created_at").first(),
        


    }
    return render(request, "home.html", context)

def downloads(request):

    site = SiteSetting.objects.first()

    downloads = Download.objects.filter(is_active=True)

    context = {
        "downloads": downloads,
        "site": site,
    }

    return render(request, "downloads.html", context)
