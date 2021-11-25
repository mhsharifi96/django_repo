

from django.urls import path
from .views import  *


urlpatterns = [
    path('theme',ShowTemplate.as_view()),
    path('',MainPageView.as_view()),
    path('detail/<int:id>/',postDetail , name='post-detail'),
    path('detail-view/<int:pk>/',PostDetailView.as_view()),

    path('simple_form/',simple_form),
    path('get-name/',get_name,name="get-name-mk"),
    path('add-tag/',add_tag_form,name="tag-mk"),
    path('edit-tag/<int:tag_id>',edit_tag_form,name="edit-tag-mk"),
    path('delete-tag/<int:tag_id>',delete_tag_form,name="delete-tag-mk"),
    path('delete-tag-direct/<int:tag_id>',delete_tag_without_form,name="delete-tag-direct"),
    path('tags',TagListView.as_view(),name='tag-list'),
    path('add-comment/',add_comment,name="add-comment"),
    path('login',login_maktab,name='login-mk'),
    path('register',register_maktab,name='register-mk'),
    path('new-password',set_new_password,name='new-pass-mk'),   
]


