from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from pages.models import Page
from products.models import Product, AffiliateTool
from downloads.models import Download

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

        affiliate_tools_list = ''
        affiliate_tools = AffiliateTool.objects.all()
        for affiliate_tool in affiliate_tools:
            affiliate_tool.html = affiliate_tool.html.replace('%%FNAME%%', request.user.first_name)
            affiliate_tool.html = affiliate_tool.html.replace('%%LNAME%%', request.user.last_name)
            #affiliate_tool.html = affiliate_tool.html.replace('%%AFFILIATELINK%%', 'aff-link')

            if (affiliate_tool.type != 'html'):
                affiliate_tool.html = '<div class="affiliatetools"><h3 class="toolname">' + affiliate_tool.name + '</h3><p class="toolcontent">' + affiliate_tool.html + '</p></div>'
            else:
                affiliate_tool.html = '<div class="affiliatetools"><h3 class="toolname">' + affiliate_tool.name + '</h3><textarea class="toolhtml">' + affiliate_tool.html + '</textarea><p class="toolcontent">' + affiliate_tool.html + '</p></div>'

            html = html.replace('%%AFFTOOL' + str(affiliate_tool.id) + '%%', affiliate_tool.html)
            affiliate_tools_list += affiliate_tool.html   
        html = html.replace('%%AFFILIATETOOLLIST%%', affiliate_tools_list)        

    
    # get affiliate information in here
    # if i even want to do this section
    #html = html.replace('%%AFFFNAME%%', affiliate.first_name)
    #html = html.replace('%%AFFLNAME%%', affiliate.first_name)
    #html = html.replace('%%AFFEMAIL%%', affiliate.first_name)
    #html = html.replace('%%AFFIDNUM%%', affiliate.first_name)
    #html = html.replace('%%AFFUSERNAME%%', affiliate.first_name)
    #html = html.replace('%%AFFCUSTOM1%%', affiliate.first_name)
    #html = html.replace('%%AFFCUSTOM2%%', affiliate.first_name)
    #html = html.replace('%%AFFCUSTOM3%%', affiliate.first_name)
    #html = html.replace('%%AFFCUSTOM4%%', affiliate.first_name)
    #html = html.replace('%%AFFCUSTOM5%%', affiliate.first_name)
    
    products = Product.objects.all()
    for product in products:
        html = html.replace('%%ORDERLINK' + str(product.id) + '%%', '/order.php?productid=' + str(product.id))
        html = html.replace('%%PRICE' + str(product.id) + '%%', product.price)
        
    # put code in here to figure out which downloads i actually have access to
    # put in "<div class=\"nodownload\"><p>This download is not yet availiable.</p></div>"
    downloads_list = '<div id="downloadslist">'
    downloads = Download.objects.all()
    for download in downloads:
    	download_content = '<div class="download"><h3 class="downloadname"><a href="/members/download.php?downloadid=' + str(download.id) + '">' + download.name + '</a></h3><p class="downloaddescription">' + download.description + '</p></div>';
        html = html.replace('%%DOWNLOAD' + str(download.id) + '%%', '/order.php?productid=' + str(product.id))
        downloads_list += download_content
        
    downloads_list += '</div>'
    html = html.replace('%%DOWNLOADSLIST%%', downloads_list)
    
    # blog processing section goes here
    
    return HttpResponse(html)