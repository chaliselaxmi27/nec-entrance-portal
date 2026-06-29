from .models import QuickLink

def footer_data(request):
    return {
        "quick_links": QuickLink.objects.filter(is_active=True).order_by("order")
    }