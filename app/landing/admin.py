from django.contrib import admin
from . import models


class CountryInline(admin.TabularInline):
    model = models.LandingCurseValue


class LandingCurseAdmin(admin.ModelAdmin):
    model = models.LandingCurse
    inlines = [CountryInline, ]


admin.site.register(models.LandingCurse, LandingCurseAdmin)
admin.site.register(models.SeoTag)
