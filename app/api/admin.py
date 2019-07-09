from django.contrib import admin

from .models import (UserProfile,
                     Restaurant,
                     Comment,
                     Reaction,
                     Ownership,
                     )

admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(Ownership)
