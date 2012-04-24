from website.models import URL

class GetSiteMiddleWare:
    def process_request(self, request):
        host = request.get_host().lower()
        request.website = URL.objects.get(full_url=host).website