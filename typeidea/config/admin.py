from django.contrib import admin

from .models import Link, SideBar
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@admin.register(SideBar, site=custom_site)
class SideBar(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')
