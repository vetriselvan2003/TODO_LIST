from django.contrib import admin

from .models import track

# Register your models here.
class fun(admin.ModelAdmin):
    list_display=["tittle"]

admin.site.register(track,fun)