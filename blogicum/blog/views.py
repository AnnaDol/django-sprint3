from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404, render
from datetime import datetime
from .models import Category, Post

MAX_POST = 5

post_list = Post.objects.filter(
        pub_date__date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template_name = 'blog/index.html'
    posts = post_list[:MAX_POST]
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        post_list,
        pk=post_id
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    categories = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_list_or_404(
        post_list,
        category__slug=category_slug
    )
    context = {
        'category': categories,
        'posts': posts
    }
    return render(request, template_name, context)
