# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from xadmin import views
from xadmin.filters import RelatedFieldListFilter
from xadmin.filters import manager
from xadmin.layout import Row, Fieldset, Container

from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Post, Category, Tag
from typeidea.base_admin import BaseOwnerAdmin


class BaseSettings:
    enable_themes = True
    use_bootswatch = True





class PostInline:  # StackedInline 样式不同
    form_layout = (
        Container(
            Row('title', 'desc')
        )
    )
    extra = 0  # 控制额外多几个
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav',)
    inlines = [PostInline, ]

    def post_count(self, obj):  # 分类下有多少篇文章
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(RelatedFieldListFilter):
    """
    自定义分类只展示当前用户分类（右侧）
    """

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(CategoryOwnerFilter, self).__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]
    list_display_links = []  # 用来配置哪些字段可以作为链接

    list_filter = ['category']
    search_fields = ['title', 'category__name']

    actions_on_top = True  # 动作
    actions_on_bottom = True

    filter_vertical = ('tag',)

    # 编辑页面
    save_on_top = True  # 编辑页面按钮

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content',
        )
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # reverse('xadmin:blog_post_change', args=(obj.id,))
            self.model_admin_url('change', obj.id)
        )

    operator.short_description = '操作'  # 指定表头的展示文案


xadmin.site.register(views.BaseAdminView, BaseSettings)
