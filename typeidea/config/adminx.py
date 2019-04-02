import xadmin

from .models import Link, SideBar


@xadmin.sites.register(Link)
class LinkAdmin:
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@xadmin.sites.register(SideBar)
class SideBar:
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content', 'status')
