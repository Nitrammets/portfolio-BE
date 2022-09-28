from django.urls import include, path
from . import views

urlpatterns = [
    path('projects/all/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('blogposts/all/', views.BlogPostList.as_view()),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view()),
]