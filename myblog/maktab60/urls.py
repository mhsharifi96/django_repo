

from django.urls import path
from .views import  *


urlpatterns = [
    path('theme',ShowTemplate.as_view()),
    path('',MainPageView.as_view()),
    path('detail/<int:pk>/',PostDetailView.as_view()),

    path('simple_form/',simple_form),
    path('get-name/',get_name,name="get-name-mk"),
    path('add-tag/',add_tag_form,name="tag-mk"),
    path('edit-tag/<int:tag_id>',edit_tag_form,name="edit-tag-mk"),
    path('delete-tag/<int:tag_id>',delete_tag_form,name="delete-tag-mk"),
    path('delete-tag-direct/<int:tag_id>',delete_tag_without_form,name="delete-tag-direct"),
    path('tags',TagListView.as_view(),name='tag-list'),
]


