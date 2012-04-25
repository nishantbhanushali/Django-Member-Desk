from profiles.models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    def queryset(self, request):
        # use our manager, rather than the default one
        qs = self.model.all_objects.get_query_set()
        
        # we need this from the superclass method
        ordering = self.ordering or () # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(UserProfile, UserProfileAdmin)