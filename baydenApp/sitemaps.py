from django.contrib.sitemaps import Sitemap
from .models import Event

class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Event.objects.all()
    
    def lastmod(self, obj):
        return obj.time_of_attendance