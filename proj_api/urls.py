from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ListPosts, ListSinglePost

urlpatterns = [
    path('token/', obtain_auth_token, name='obtain'),
    path('posts/', ListPosts.as_view(), name='list-posts'),
    path('posts/<str:pk>/', ListSinglePost.as_view(), name='list-single-post'),
]
