from config.models import Config
from django.contrib.sites.models import Site
from django.contrib.sites.middleware import CurrentSiteMiddleware

class LoadConfigMiddleware(CurrentSiteMiddleware):
     def process_request(self, request):
        request.site =  Config.objects.get_current()
