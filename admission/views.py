from django.shortcuts import render, get_object_or_404
from .models import Notice




def notice_list(request):
    notices = Notice.objects.order_by('-published_date')

    context = {
        'notices': notices
    }

    return render(request, 'admission/notice_list.html', context)


def notice_detail(request, slug):
    notice = get_object_or_404(Notice, slug=slug)

    context = {
        'notice': notice
    }

    return render(request, 'admission/notice_detail.html', context)
