from django.urls import path
from django.views.generic import TemplateView
from .views import (GetListsView, getTasks, ListCreateView,
                    TaskCreateView, ListUpdateView, ListDeleteView, markAsComplete, TaskUpdateView,
                    TaskDeleteView, markTaskAsComplete)

urlpatterns = [
    path('', GetListsView.as_view(), name='homepage'),
    path('new-list/', ListCreateView.as_view(), name='new-list'),
    path('new-task/<int:list_id>/', TaskCreateView.as_view(), name='new-task'),
    path('warning/', TemplateView.as_view(template_name='warning.html'), name='warning'),
    path('update-list/<int:pk>/', ListUpdateView.as_view(), name='update-list'),
    path('mark-as-complete-list/<int:pk>/', markAsComplete, name='mark-as-complete-list'),
    path('delete-list/<int:pk>/', ListDeleteView.as_view(), name='delete-list'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
    path('mark-as-complete-task/<int:pk>/', markTaskAsComplete, name='mark-as-complete-task'),
    path('<str:pk>/', getTasks, name='tasks'),

]
