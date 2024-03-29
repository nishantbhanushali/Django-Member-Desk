from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^dashboard/", include("dashboard.urls")),
    url(r"^members/", include("members.urls")),
    url(r"^pages/", include("pages.urls")),
    url(r"^blogs/", include("blogs.urls")),    
    url(r"^sales/", include("sales.urls")),
    url(r"^about/", include("about.urls")),
    url(r"^website/", include("website.urls")),
    url(r"^downloads/", include("downloads.urls")),
    url(r"^products/", include("products.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
