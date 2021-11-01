from django.contrib import admin
from django.contrib.auth.models import User, Group
from admin_interface.models import Theme
from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Theme)

admin.site.register(MainBanner)
admin.site.register(MetaTags)
