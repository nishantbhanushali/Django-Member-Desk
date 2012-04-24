from website.models import URL
from django.conf import settings

class GetSiteMiddleWare:
    def process_request(self, request):
        host = request.get_host().lower()
        settings.website = URL.objects.get(full_url=host).website

class disableCSRF:
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        return None