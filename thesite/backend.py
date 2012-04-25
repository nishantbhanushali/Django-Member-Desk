from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.http import HttpResponse

class EmailOrUsernameModelBackend(object):
    def authenticate(self, email=None, password=None):
        kwargs = {'email': email}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                 try:
                     profile = user.get_profile()
                     return user
                 except UserProfile.DoesNotExist:
                     return None
            else:
                 return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            try:
                profile = user.get_profile()
                return user
            except UserProfile.DoesNotExist:
                return None
        except User.DoesNotExist:
            return None