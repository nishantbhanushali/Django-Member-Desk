from django.shortcuts import render_to_response
from pages.models import Page
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def public(request, url):
    page = get_object_or_404(Page, location=url)
    
    page.layout.html = page.layout.html.replace('%%BODY%%', page.html)
    
    return HttpResponse(page.layout.html)