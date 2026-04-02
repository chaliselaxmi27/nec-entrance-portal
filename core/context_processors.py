from admission.models import Notice

def latest_notices(request):
    notices = Notice.objects.order_by('-published_date')[:8]
    return {
        'latest_notices': notices
    }