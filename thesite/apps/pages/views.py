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
    
    #html = html.replace('%%AWEBERLISTNAME%%', page.website.aweber)
    #html = html.replace('%%SUBDOMAIN%%',page.website.subdomain)
	#html = html.replace('%%SITEDOMAIN%%',page.website.domain)
    html = html.replace('%%SITENAME%%',page.website.name)
    html = html.replace('%%REGISTRATION%%','/register.php')
    
    if request.user.is_authenticated():
        html = html.replace('%%FNAME%%', request.user.first_name)
        html = html.replace('%%LNAME%%', request.user.last_name)
        html = html.replace('%%AFFILIATEID%%', str(request.user.id))
        #html = html.replace('%%AFFILIATELINK%%', 'aff-link')
        html = html.replace('%%LNAME%%', request.user.last_name)
        #html = html.replace('%%UUID%%', request.user.uuid)
        #html = html.replace('%%CUSTOM1%%', request.user.custom1)
        #html = html.replace('%%CUSTOM2%%', request.user.custom2)
        #html = html.replace('%%CUSTOM3%%', request.user.custom3)
        #html = html.replace('%%CUSTOM4%%', request.user.custom4)
        #html = html.replace('%%CUSTOM5%%', request.user.custom5)
    
    # get affiliate information in here
    html = html.replace()

    return HttpResponse(html)