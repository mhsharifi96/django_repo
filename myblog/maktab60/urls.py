

from django.urls import path
from .views import  ShowTemplate,MainPageView,PostDetailView


urlpatterns = [
    path('theme',ShowTemplate.as_view()),
    path('',MainPageView.as_view()),
    path('detail/<int:pk>',PostDetailView.as_view()),
]


