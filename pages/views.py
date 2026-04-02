from django.shortcuts import render
from core.models import SiteSetting, HeroSlide
from admission.models import Notice, Requirement, Scholarship
from programs.models import Program
from .models import Download




def home(request):
    context = {
        "site": SiteSetting.objects.first(),
        "hero_slides": HeroSlide.objects.filter(is_active=True).order_by("order"),
        "latest_notices": Notice.objects.all()[:10],
        "requirements": Requirement.objects.all(),
        "scholarships": Scholarship.objects.all(),
        "programs": Program.objects.filter(is_active=True).order_by("display_order"),
        "home_downloads": Download.objects.filter(is_active=True).order_by("order", "-created_at"),

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