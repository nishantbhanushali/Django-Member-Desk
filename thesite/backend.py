from django.conf import settings
from django.contrib.auth.models import User

class EmailOrUsernameModelBackend(object):
    def authenticate(self, email=None, password=None):
        kwargs = {'email': email}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None