from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.views.generic import DetailView


def index(request):
    posts = Post.objects.order_by("-timestamp")
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)

    context = {
        'post_list': post_list,
        'posts': posts,
        'is_paginated': True,
    }
    return render(request, 'index.html', context)


class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['photos'] = PostImage.objects.all()
        return context


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def get_category_count():
    queryset = Post.objects.values(
        'categories__name').annotate(Count('categories__name'))
    return queryset


def browse(request):
    category_count = get_category_count()
    posts = Post.objects.order_by("-timestamp")
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)

    context = {
        'post_list': post_list,
        'posts': posts,
        'is_paginated': True,
        'category_count': category_count,
    }
    return render(request, 'browse.html', context)


def search(request):
    category_count = get_category_count()
    queryset = Post.objects.order_by("-timestamp")
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(categories__name__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'is_paginated': True,
        'category_count': category_count,
    }
    return render(request, 'search_results.html', context)
