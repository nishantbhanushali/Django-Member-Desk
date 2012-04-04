from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "dashboard/home.html"}, name="dashboard"),
    url(r"^what_next/$", direct_to_template, {"template": "dashboard/what_next.html"}, name="what_next"),
)
