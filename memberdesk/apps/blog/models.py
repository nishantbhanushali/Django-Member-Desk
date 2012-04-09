from django.db import models
import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.utils import A

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog)
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    html = models.TextField()
    level = models.ForeignKey(Level)
    layout = models.ForeignKey(Layout)
    days_required = models.IntegerField()
    date_required = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
class Blog(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    html = models.TextField()
    affiliate_visible = models.BooleanField()
    members_only = models.BooleanField()
    level = models.ForeignKey(Level)
    layout = models.ForeignKey(Layout)
    order = models.IntegerField()
    days_required = models.IntegerField()
    date_required = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    post = models.ForeignKey(BlogPost)
    content = models.TextField()
    author_name = models.CharField(max_length=128)
    author_email = models.EmailField()
    author = models.ForeignKey(Member)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    
class BlogTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/page/1">Edit</a>')
    class Meta:
        model = Blog
        attrs = {'class': 'table table-striped'}

class BlogPostTable(tables.Table):
    edit = tables.TemplateColumn('<a class="btn" href="/page/1">Edit</a>')
    class Meta:
        model = BlogPost
        attrs = {'class': 'table table-striped'}