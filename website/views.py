from django.shortcuts import render


def index(request):
    context = {
        'posts': None
    }
    return render(request, 'blog/index.html', context=context)


def details(request, pk=None):
    context = {
        'post': None
    }
    return render(request, 'blog/post.html', context=context)


def create(request):
    context = {}
    return render(request, 'blog/create.html', context=context)
