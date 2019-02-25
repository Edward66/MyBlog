from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'the1fire'
    site_title = 'the1fire后台管理'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')  # 反向解析的名字
