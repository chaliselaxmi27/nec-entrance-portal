from django.contrib import admin
from .models import SiteSetting, HeroSlide

admin.site.register(SiteSetting)
admin.site.register(HeroSlide)
admin.site.site_header = "NEC Entrance Administration"
admin.site.site_title = "NEC Admin Portal"
admin.site.index_title = "Welcome to NEC Management Panel"