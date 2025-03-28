from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.utils import timezone

from .models import Category, Post

MAX_POST = 5


def get_post_list():
    post_list = Post.objects.filter(
        pub_date__date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return post_list


def index(request):
    template_name = 'blog/index.html'
    posts = get_post_list()[:MAX_POST]
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        get_post_list(),
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
    posts = get_post_list().filter(
        category__slug=category_slug
    )
    context = {
        'category': categories,
        'posts': posts
    }
    return render(request, template_name, context)
