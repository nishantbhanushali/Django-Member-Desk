from django.db import models
from website.models import Level, Website, URL
from manager import WebsiteSpecificManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

def current_site():
    return settings.website
            
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.ForeignKey(Website, default=current_site)
    
    affiliate_id = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    #referrer = models.ForeignKey(User)
    override = models.IntegerField()
    level = models.ForeignKey(Level)
    custom1 = models.CharField(max_length=128)
    custom2 = models.CharField(max_length=128)
    custom3 = models.CharField(max_length=128)
    custom4 = models.CharField(max_length=128)
    custom5 = models.CharField(max_length=128)    
    
    objects = WebsiteSpecificManager()
    all_objects = models.Manager()
    
def get_user_by_email(email):
    try:
        for user in User.objects.filter(email=email):
            try:
                profile = user.get_profile()
                return user
            except UserProfile.DoesNotExist:
                continue
            return None
    except User.DoesNotExist:
        return None
    
    except UserProfile.DoesNotExist:
        return None

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)