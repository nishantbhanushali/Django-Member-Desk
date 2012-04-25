from django.db import models
from website.models import Level, Website
from manager import WebsiteSpecificManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
            
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.ForeignKey(Website)
    
    affiliate_id = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    uuid = models.CharField(max_length=128)
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

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)