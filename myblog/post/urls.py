from django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name = 'post'
urlpatterns = [
    
    path('',index,name='index'),
    path('today',today_date),
    path('my/<int:coustom_id>/<str:name>/',my_view),
    path('my2/<int:id>/',my_view_2),
    path('detail/<int:id>/',detail_post,name='detail'),
    path('category/',category),
    path('category/<int:cat_id>/',category_detail,name='category_detail'),
    path('base/',base_temp_view),

    # on class 
    path('class_today/',class_today_time,name=""),
    # path('class_detail_post/',class_detail_post), #step 1 بدون پارامتر ورودی
    path('class_detail_post/<int:post_id>',class_detail_post),
    path('class_first_template/',class_first_template),
    path('class_post_detail/<int:post_id>',class_post_detail,name="class_detail"),
    path('class_post_list/',class_post_list),
    path('same_template_name/',same_template_name),
    path('show_theme/',show_theme),
    path('simple_form/',simple_form),
    # class view
    path('about/', TemplateView.as_view(template_name="new/about.html"),name="about_page"),
    path('about-view/', AboutView.as_view()),
    path('post-list-view/', PostListView.as_view()),
    path('post-detail-view/<int:pk>/', PostDetailView.as_view()),
    # start form django and custom auth
    path('get_name/', get_name),
    
    path('category_form/', category_form),
    path('category_form_edit/', category_form_edit),
    path('login/', mylogin ,name="login"),
    path('register/', myRegister ,name="register"),
    path('sec/', security_page ,name="sec"),
    path('new-password/', new_password ,name="new-password"),
    path('simple-post/', simple_post ,name="simple-post"),
    
 
    


]
