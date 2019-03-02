# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    if tag_id:
        try:
            tag = Tag.get_tag(tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list = post_list.filter(category_id=category_id)
    return render(request, 'blog/list.html', context={'post_list': post_list})


def post_detail(request, post_id):
    try:
        post = Post.get_post(post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, 'blog/detail.html', context={'post': post})
