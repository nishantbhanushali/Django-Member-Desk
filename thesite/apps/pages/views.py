from django.shortcuts import render_to_response
from pages.models import Page
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def public(request, url):
    page = get_object_or_404(Page, location=url)
    
    error = request.GET.get('e', '')
    message = request.GET.get('m', '')        
    
    html = page.layout.html.replace('%%BODY%%', page.html)
    
    html = html.replace('%%PAGEID%%', str(page.id))
    html = html.replace('%%ERROR%%', error)
    html = html.replace('%%MESSAGE%%', message)
    html = html.replace('%%CSSSTYLES%%', "<link rel=\"stylesheet\" type=\"text/css\" href=\"/css/style.css\" />")
    html = html.replace('%%PAGETITLE%%', page.title)
    html = html.replace('%%PAGELINK%%', page.location)

    
    return HttpResponse(html)