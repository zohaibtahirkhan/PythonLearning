from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('<str:pk>/', views.PostDetailView.as_view(), name='blog-post'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),

]
