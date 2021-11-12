from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    import datetime
    # post = Post.objects.get(id=1)
    posts =Post.objects.filter(id__gte=2)
    return render(request,
            'index.html',
            {"posts":posts} )