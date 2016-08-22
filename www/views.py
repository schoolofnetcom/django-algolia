from django.shortcuts import render

from www.models import Post


def index(request):
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'show.html', {'post':post})