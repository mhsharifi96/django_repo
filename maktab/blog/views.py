from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# 127.0.0.1:8000/blog

def index(request):
    # pass
    a = 2+2
    return HttpResponse(a)

def index2(request):
    # pass
    return HttpResponse('hello maktab for index2')


# post
# listpost
# likepost
# dislikepost
# viewpost
# hashtag
# follwer
# commet


# blog/test index or index2