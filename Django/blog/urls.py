from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserListView.as_view(), name='user-blogs'),
    path('about/', views.about, name='blog-about'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name='blog-post'),
    path('post/<str:pk>/update', views.PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<str:pk>/delete', views.PostDeleteView.as_view(), name='blog-post-delete'),

]
