from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse
from pages.views import public

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