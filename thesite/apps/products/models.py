from django.db import models
from website.models import Website, Level
from pages.models import Page

class Product(models.Model):
    website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    puid = models.CharField(max_length=128)
    clickbank_number = models.IntegerField()
    affiliate_commission = models.CharField(max_length=128)
    jv_commission = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    payment_type = models.CharField(max_length=128)
    time_num = models.IntegerField()
    time_type = models.CharField(max_length=128)
    upgrades_to_level = models.ForeignKey(Level)
    thank_you_page = models.ForeignKey(Page)

    trial1_price = models.CharField(max_length=128)
    trial1_time_num = models.IntegerField()
    trial1_time_type = models.CharField(max_length=128)

    trial2_price = models.CharField(max_length=128)
    trial2_time_num = models.IntegerField()
    trial2_time_type = models.CharField(max_length=128)

    created = models.DateTimeField()
    modified = models.DateTimeField()
    
class Email(models.Model):
    website = models.ForeignKey(Website)
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    body = models.TextField()
    type = models.CharField(max_length=128)
    active = models.BooleanField()

    created = models.DateTimeField()
    modified = models.DateTimeField()    

class AffiliateTool(models.Model):
    website = models.ForeignKey(Website)
    name = models.CharField(max_length=128)
    html = models.TextField()
    type = models.CharField(max_length=128)
    active = models.BooleanField()

    created = models.DateTimeField()
    modified = models.DateTimeField()