from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.utils import A

class Member(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField() 
    date_joined = models.DateTimeField()
    
class MemberTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/members/1">Edit</a>')
    class Meta:
        model = Member
        attrs = {'class': 'table table-striped'}