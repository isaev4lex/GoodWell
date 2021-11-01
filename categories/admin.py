from django.contrib import admin
from .models import *

# admin.site.register(Category)
admin.site.register(MetaTags)
admin.site.register(FlameRetard)
admin.site.register(Fitting)
# admin.site.register(Tubes)
admin.site.register(Alarm)


class PostTechAdmin(admin.StackedInline):
    model = TechnicInfo


@admin.register(Paint)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTechAdmin]

    class Meta:
        model = Paint


class PostTubeAdmin(admin.StackedInline):
    model = TechnicTubesInfo


@admin.register(Tubes)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTubeAdmin]

    class Meta:
        model = Tubes
