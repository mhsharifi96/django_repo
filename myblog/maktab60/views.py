from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse

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
    model = Post   #===> Post.object.all()
    # templates/<app_name : maktab60>/<model : post> =>tmeplates/maktab60/post_list.html
    template_name = "maktab60/index.html"
    context_object_name = 'posts' # object_list



class PostDetailView(DetailView):
    model = Post
    # templates/<app_name : maktab60>/<model : post> =>tmeplates/maktab60/post_detail.html
    template_name = "maktab60/detail.html" 



def simple_form(request):
    print(request)
    print(request.method)
    print('post : ',request.POST)
    print('get : ',request.GET)
    # print(request.POST['email'])  # چون دفعه اول با get
    message = ''
    if(request.method == 'POST'):

        # if(request.POST['search']):
        #     filter_posts = Post.objects.filter(title_contains=request.POST['search'])
        if(request.POST['email'] == 'maktab'):
            message = {'text':"سلام مکتب شریف" ,'class_css':'text-danger'}
        else : message = {'text':"سلام دوست من" ,'class_css':'text-primary'}
        
    return render(request,'maktab60/simple_form.html',{'message':message})




