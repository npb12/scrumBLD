from django.contrib import admin

from users.models import UserProfile, Message, Associate

admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Associate)
