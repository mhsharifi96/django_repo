from django.urls import path
from .views import *
# app_name = 'post'
urlpatterns = [
    
    path('',index),
    path('today',today_date),
    path('my/<int:coustom_id>/<str:name>/',my_view),
    path('my2/<int:id>/',my_view_2),
    path('detail/<int:id>/',detail_post,name='detail'),
    path('category/',category),
    path('category/<int:cat_id>/',category_detail,name='category_detail'),
    path('base/',base_temp_view),

    # on class 
    path('class_today/',class_today_time),
    # path('class_detail_post/',class_detail_post), #step 1 بدون پارامتر ورودی
    path('class_detail_post/<int:post_id>',class_detail_post),
    path('class_first_template/',class_first_template),
    path('class_post_detail/<int:post_id>',class_post_detail),
    path('class_post_list/',class_post_list),
    


]
