from core.models import SiteSetting
from admission.models import Notice

def global_site_data(request):
    return {
        "site": SiteSetting.objects.last(),
        "latest_notices": Notice.objects.all()[:10],
    }