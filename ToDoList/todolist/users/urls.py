from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, user_logout

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]

