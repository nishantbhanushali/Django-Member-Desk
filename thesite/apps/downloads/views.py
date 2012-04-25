from django.shortcuts import redirect
from django.http import HttpResponse
from downloads.models import Download
import datetime

def get_file(request, id):
    download = get_object_or_404(Download, pk=id)
    now = datetime.datetime.now()
    
    # have to check if http is in filename somewhere
    
    if download.type == 'public':
        return redirect('http://s3.memberdesk.com/' + str(settings.website.id) + '/' + download.filename)
	else:
	    if not request.user.is_authenticated():
	        return HttpResponse("You must be logged in to access this download.")
	    else:
	        if request.user.days < download.days_required:
                return HttpResponse("You haven't been a member long enough to access this file.")
            elif download.date > now
            	return HttpResponse("This download is not yet available.")
            elif download.level.number > request.user.level.number
                return HttpResponse("Your level of membership cannot access this download.")
            else:
                return redirect('http://s3.memberdesk.com/' + str(settings.website.id) + '/' + download.filename)