from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from datetime import datetime
# models
from .models import  Post,Category,Tag

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
    # return render(request,'list_post_main_temp.html',{'posts':posts})

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





# start form
from .forms import SimpleForm,SimpleModelForm,LoginForm,UserFormModel,NewPasswordForm,SimplePostModelForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def get_name(request):
    
    form = SimpleForm()

    if request.method == "POST":

        form = SimpleForm(request.POST)
        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            print('name',form.cleaned_data['name'])
            # newtag = Tag()
            # newtag.title =  form.cleaned_data['name']
            form.save()
        # else :
        #     print(form.cleaned_data)
            # 
    return render(request,'forms/name_form.html',{
        'form':form
    })


def category_form (request):


    form = SimpleModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect(reverse('post:about_page'))
    return render(request,'forms/category_form.html',{
        'form':form
    })



def category_form_edit(request):

    category = Category.objects.get(id=1)
    form = SimpleModelForm(request.POST or None,instance=category)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect(reverse('post:about_page'))

    return render(request,'forms/category_form.html',{
        'form':form
    })




#end form


def mylogin(request):
    #refrence :  https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(request,username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                print(user)
                login(request,user)
                return redirect(reverse('post:sec'))
            else :
                print('not found user')
    return render(request,'forms/login.html',{'form':form})



@login_required(login_url='/blog/login')
def security_page(request):

    return HttpResponse('this page need to login :|')

from django.contrib.auth.models import User
def myRegister(request):
    form = UserFormModel(None or request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
            print('new user register is :',user)
    
    return render(request,'forms/register.html',{'form':form})


@login_required(login_url='/blog/login')
def new_password(request):
    user = request.user
    print(user.is_authenticated)
    print(user.check_password('12345555'))
    form = NewPasswordForm(None or request.POST)
    print(form)
    if  user.is_authenticated : 
        if request.method == "POST":
            if form.is_valid():
                if user.check_password(form.cleaned_data['password']):
                    user.set_password(form.cleaned_data['password_1'])
                    user.save()
                    # return HttpResponse('password changed ')
                

    return render(request,'forms/new_password.html',{'form':form})




def simple_post(request):
    # refrence : https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/#handling-uploaded-files-with-a-model
    if request.method == 'POST':
        print(request.FILES)
        form = SimplePostModelForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            
    else:
        form = SimplePostModelForm()
    # return render(request,'forms/add_simple_post.html',{'form':form})
    return render(request,'forms/add_simple_post_manual.html',{'form':form})



# add css class to forms    
#refrence : https://stackoverflow.com/questions/401025/define-css-class-in-django-forms