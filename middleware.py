from django.conf import settings
from django.contrib.sites.models import Site

class MultisiteMiddleware:
    
    def process_request(self, request):
        
        splitStr = request.get_host().split(":")
        host = splitStr[0]
        
        site_id = -1
        try:
            site = Site.objects.get(domain=host)
            site_id = site.id
            print "found site: " + str(site) + "for host: " + request.get_host()
        except Site.DoesNotExist:
            print "No Site found for host: " + request.get_host()
            pass
        
        if site_id > -1:
            settings.SITE_ID = site.id
            
        
        