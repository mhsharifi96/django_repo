from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import SimpleForm,TagForm,TagModelForm,TagDeleteModelForm,CommentModelForm,LoginForm,UserRegisterFormModel,SetNewPasswordForm
from django.contrib import messages


# Create your views here.
from post.models import Post,Category,Tag



# نمایش جزییات پست 
def postDetail(request,id):
    # url add nashode
    post = Post.objects.get(id=id) #try except OR get_object_or 404
    form = CommentModelForm()
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # return redirect(reverse('post-detail',id=id)) #

    return render(request,'maktab60/detail.html',{'post':post,'form':form})

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




# form 


def get_name(request):
    form = SimpleForm()
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print('form valid ')
            # model save 
            
    
    return render(request,'maktab60/forms/name_form.html',{'form':form})

@login_required(login_url='/maktab60/login')
def add_tag_form (request):
    my_message = ""
    # form = TagForm()
    form = TagModelForm()
    print(request.user.email)
    if request.method == "POST":
        form = TagModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.add_message(request, messages.ERROR, f'تگ مورد نظر ذخیره گردید.',extra_tags="danger")
          

            return redirect(reverse('tag-list')) #app_name:name_url

    return render(request,'maktab60/forms/tag_form.html',{
        'form':form,
        
        

    })


# باید اول اون چیزی که میخواییم اپدیت کنیم از دیتابیس پیدا کنیم
def edit_tag_form (request,tag_id):
    tag = get_object_or_404(Tag,id=tag_id)
    form = TagModelForm(instance=tag)  #validate

    if request.method == "POST":
        form =TagModelForm(request.POST,instance=tag)  #validate
        if form.is_valid():
            form.save()
            return redirect(reverse('tag-list')) #app_name:name_url

    return render(request,'maktab60/forms/edit_tag_form.html',{'form':form,'tag':tag})


def delete_tag_form(request,tag_id):
    
    tag = get_object_or_404(Tag,id=tag_id)
    
    form = TagDeleteModelForm(instance=tag)  #validate
    if request.method == "POST":
        tag.delete()
        print('delete')
        return redirect(reverse('tag-list')) #reverse('app_name:name_url')


    return render(request,'maktab60/forms/delete_tag_form.html',{'form':form,'tag':tag})


def delete_tag_without_form(request,tag_id):
    
    tag = get_object_or_404(Tag,id=tag_id)    
    tag.delete()
    print('delete')
    return redirect(reverse('tag-list')) #reverse('app_name:name_url')



def add_comment(request):
    #برای پست اولی میخواهیم کامتی بگذاریم
    post = Post.objects.get(id=1)
    form = CommentModelForm()
    if request.method == "POST":
        form =CommentModelForm(request.POST)  #validate
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            

            return HttpResponse('this comment saved')
    return render(request,'maktab60/forms/add_comment.html',{'form':form,'post':post})


# def detail_post
#  get post and comment
#  form comment
# render page




def login_maktab(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username= form.cleaned_data.get('username'),password= form.cleaned_data.get('password'))
            if user is not None :
                login(request,user)
                
                return redirect(reverse('tag-mk')) #
            
            print('userrrrrrrrrrrrrrr :',user)

            # cleaned_data
    return render(request,'maktab60/forms/login.html' ,{'form':form})


def register_maktab(request):
    form = UserRegisterFormModel(None or request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
            print('new user register is :',user)
            return HttpResponse('user register :)')
    
    return render(request,'maktab60/forms/register.html',{'form':form})

@login_required(login_url='/maktab60/login')
def set_new_password(request):
    form = SetNewPasswordForm()
    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            print(user)
            print(user.check_password(form.cleaned_data.get('password')))
            if user.check_password(form.cleaned_data.get('password')):
                password=user.set_password(form.cleaned_data.get('password1'))
                print('password:',password)
                user.save()

            print('user request : ',request.user)
        
    return render(request,'maktab60/forms/set_new_password.html',{'form':form})





class TagListView(ListView):
    # model = Tag
    queryset = Tag.objects.all().filter(title__contains="a")
    template_name = "maktab60/tag_list.html"
   

        
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context['category'] = Category.objects.all()
        print(context)
        
        return context


class searchPageView(ListView):
    # model = Post   
    #queryset
    template_name = "maktab60/search.html"
    context_object_name = 'posts' # object_list

    def get_queryset(self):
        # print('kwargs',self.kwargs)
        
        queryset = Post.objects.all()
        
        q = self.request.GET.get('q')
        if q :
            queryset = queryset.filter(title__contains= q)
            
        return queryset
