from django.shortcuts import render, get_object_or_404
from .models import Program


def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)

    context = {
        "program": program,
    }

    return render(request, "programs/program_detail.html", context)