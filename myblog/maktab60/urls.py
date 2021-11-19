

from django.urls import path
from .views import  ShowTemplate,MainPageView,PostDetailView,simple_form


urlpatterns = [
    path('theme',ShowTemplate.as_view()),
    path('',MainPageView.as_view()),
    path('detail/<int:pk>/',PostDetailView.as_view()),
    path('simple_form/',simple_form)
]


