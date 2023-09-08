from django.contrib import admin
from .models import *

@admin.register(links)
class linksadmin(admin.ModelAdmin):
    list_display=["id",'Links',"datetime"]