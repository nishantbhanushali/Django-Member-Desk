from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"

urlpatterns = patterns("",
    url(r"^$", 'pages.views.public', name="home"),
    url(r"^members/?$", 'pages.views.members'),
    url(r"^login/?$", 'profiles.views.login_view'),    
    url(r"^register/?$", 'profiles.views.register_view'),    
    url(r"^download/(?P<id>\d+)$", 'downloads.views.get_file'),    

    url(r"^admin/invite_user2/$", "pinax.apps.signup_codes.views.admin_invite_user", name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )