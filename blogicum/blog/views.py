from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404, render
from datetime import datetime
from .models import Category, Post

def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.all().filter(
        pub_date__date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.all().filter(
            pk=post_id
        ),
        Q(pub_date__date__lte=datetime.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    categories = get_object_or_404(
        Category.objects.all().filter(
            slug=category_slug
        ),
        is_published=True
    )
    posts = get_list_or_404(
        Post.objects.all().filter(
            pub_date__date__lte=datetime.now(),
            category__slug=category_slug
        ),
        is_published=True
    )
    context = {
        'category': categories,
        'posts': posts
    }
    return render(request, template_name, context)
