from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound

from .models import Post
from datetime import datetime
# models
from .models import  Post,Category

#start class 

# localhost:8000/blog/today/
def class_today_time(request):
    # a = 2+2
    print(request)
    print(request.path)
    print(request.body)
    print(request.method)
    print(request.GET)
    print(request.POST)
    return  HttpResponse(f" today is : {datetime.today()}")



def class_detail_post(request,post_id):

    print(post_id)
    # post id 2 
    # id = 
    # post = get_object_or_404(Post,id=post_id)
    try :
        post  = Post.objects.get(id=post_id)
        body = f"<html><body><h1>{post.title}</h1><p>{post.desc}</p></body></html>"
    except Post.DoesNotExist :
        body = "ارباب یافت نشد"
        # return HttpResponseNotFound(body)
    # title = "maktab sharif"
    # desc = "desc sample"
    return  HttpResponse(body)

# django ->url ---->view ---->response

def class_first_template(request):

    today = datetime.today()
    title = "maktab coustom"
    post = Post.objects.get(id=2)
    # context = {'today':today,'title':title,'post':post}
    return render(request,'maktab.html',{'post':post})


def class_post_detail(request,post_id):
    # نمایش محتویات پست
    
    post = Post.objects.get(id=post_id)
    
    return render(request,'class_post_detail.html',{'post':post})


def class_post_list(request):
    posts = Post.objects.all().order_by('?')
    for post in posts :
        print(post)
    return render(request,'class_post_list.html',{'posts':posts})

# end class


# start 19 nov
def same_template_name(request):
    return render(request,'new/same_name.html')


def show_theme(request):
    # note part3 front --->static
    return render(request,'new/first_page.html')
    # return render(request,'new/second_page.html')


def simple_form(request):
    print(request.body)
    print(request.method)
    print(request.POST)
    message = ""
    if(request.method =="POST"):
        print(request.POST['email'])
        if (request.POST['email'] == 'virux'):
            message = {'text':"اجازه ثبت نام موجود نیست", 'css_class':'text-danger'}
        else : 
            message = {'text':"اوکی داداش",'css_class':"text-primary"}
        # if need query u can run it 
        # e.x : user.objects.create(...)
        # return redirect('index')
    
    return render(request,'new/simple_form.html',{'message':message})


## class view###
from django.views.generic import TemplateView,ListView,DetailView

class AboutView(TemplateView):
    # more : https://docs.djangoproject.com/en/3.2/topics/class-based-views/#subclassing-generic-views
    template_name = "new/about.html"

class PostListView(ListView):
    # https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/
    model = Post

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    #more  https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/  
    model= Post



# end























































# نمایش تاریخ و ساعت امروز
def today_date(request):
    #request :  https://docs.djangoproject.com/en/3.2/ref/request-response/
    #view :  https://docs.djangoproject.com/en/3.2/topics/http/views/
    print(request.body)
    print(request.method)
    print(request.path_info)
    print(request.path)
    print(request.POST)
    print(request.GET)

    today = datetime.today()
    html = f'<p>today is : {today}</p>'
    return HttpResponse(html)


def my_view (request,coustom_id,name='mohammad'):

    print(coustom_id)
    print(request.path)
    print(request.GET)

    
    if (coustom_id==1):
        print('ok')
        return HttpResponse(f'my name is {name}')
    return HttpResponseNotFound('not found') #404


def my_view_2 (request,id):
    post = {
        'title':id,
        'body' : "this is first body ...",
        'today' : datetime.today()
    }

    return render(request,'first.html',post)


def detail_post (request,id):
    print('id',type('id'))
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist :
        # return HttpResponseNotFound(f'آیدی {id} موجود نیست ارباب')
        return render(request,'first.html',{'post':None})
    print(post)
    return render(request,'first.html',{'post':post})

# def detail_post(request)
#     #هدف اولیه : پستی با ایدی دو را نمایش دهیم
#     post = Post.objects.get(id=2)


def index(request):

    
    posts =Post.objects.all().order_by('-created_on')
    category = Category.objects.all()
    return render(request,
            'index.html',
            {"posts":posts,"category":category} )


def category(request) : 
    category = Category.objects.all()
    return render(request,'category.html',{'category':category})


def category_detail(request,cat_id):
    # category/id
    posts = Post.objects.filter(category__pk = cat_id)
    
    return render (request,'category_post.html',{'posts':posts})


def base_temp_view (request):
    return render (request,'base.html')







