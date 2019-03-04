# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post, Tag, Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)

    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list, category = Post.get_by_category(category_id)

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
    }
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, 'blog/detail.html', context={'post': post})
