from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.utils import A

class Product(models.Model):
    name = models.CharField(max_length=128)
    puid = models.CharField(max_length=128)
    clickbank_number = models.IntegerField()
    affiliate_commission = models.CharField(max_length=128)
    jv_commission = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    payment_type = models.CharField(max_length=128)
    time_num = models.IntegerField()
    time_type = models.CharField(max_length=128)
    upgrades_to_level = model.ForeignKey(Level)
    thank_you_page = model.ForeignKey(Page)

    trial1_price = models.CharField(max_length=128)
    trial1_time_num = models.IntegerField()
    trial1_time_type = models.CharField(max_length=128)

    trial2_price = models.CharField(max_length=128)
    trial2_time_num = models.IntegerField()
    trial2_time_type = models.CharField(max_length=128)

    created = models.DateTimeField()
    modified = models.DateTimeField()
        
class MemberTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/members/1">Edit</a>')
    class Meta:
        model = Member
        attrs = {'class': 'table table-striped'}