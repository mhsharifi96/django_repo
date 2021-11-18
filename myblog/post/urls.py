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
    path('base/',base_temp_view)


]
