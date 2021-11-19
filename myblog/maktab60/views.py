from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.
from post.models import Post,Category,Tag



# نمایش جزییات پست 
def postDetail(request,id):
    # url add nashode
    post = Post.objects.get(id=id) #try except OR get_object_or 404
    return render(request,'maktab60/detail.html',{'post':post})

# نمایش لیست پست ها
def postList(request):
    # url add nashode
    posts = Post.objects.all()  # ---> get_list_or_404
    category = Category.objects.all()
    return render(request,'maktab60/list.html',{'posts':posts,'category':category})



class ShowTemplate(TemplateView):
    template_name = "theme.html"


# class MainPageView(TemplateView):
#     template_name = "maktab60/index.html"

class MainPageView(ListView):
    model = Post
    template_name = "maktab60/index.html"
    context_object_name = 'posts' # object_list



class PostDetailView(DetailView):
    # model = Post
    template_name = "maktab60/detail.html" 
