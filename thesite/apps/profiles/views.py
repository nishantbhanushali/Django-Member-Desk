from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from pages.views import public
from profiles.models import get_user_by_email
import uuid

def login_view(request):
    if request.method == 'GET':
        return public(request, "login")
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/members')
            else:
                return HttpResponse("Disabled Account")
        else:
            return HttpResponse("Invalid Login")
            
def register_view(request):
    if request.method == 'GET':
        return public(request, "register")
    elif request.method == 'POST':
        username = uuid.uuid4()
        data = request.POST.copy()
                
        if get_user_by_email(data['email']) is not None:
            return HttpResponse("Email Address Already In Use")

        if data['fname'] == '':
            return HttpResponse("Name is blank")

        if data['email'] == '':
            return HttpResponse("Email is blank")

        if data['password'] == '':
            return HttpResponse("Password is blank")
        
        if data['password'] != data['password2']:
            return HttpResponse("Passwords Do Not Match")

    	user = User.objects.create_user(username, data['email'], data['password'])
    	user.first_name = data['fname']
    	user.save()
    	
    	return redirect('/members')

		#set jv status
		#set ip
		#set referrer
		#set level
		#set affiliate id