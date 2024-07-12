from django.urls import path
from .views import ListLists, ListTasks, UpdateList, UpdateTask, CreateList, CreateTask, DeleteList, DeleteTask
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('lists/', ListLists.as_view(), name='lists-api'),
    path('new-list/', CreateList.as_view(), name='create-list-api'),
    path('new-task/', CreateTask.as_view(), name='create-task-api'),
    path('list/<str:pk>/', ListTasks.as_view(), name='tasks-api'),
    path('update-list/<str:pk>/', UpdateList.as_view(), name='update-list-api'),
    path('update-task/<str:pk>/', UpdateTask.as_view(), name='update-task-api'),
    path('delete-list/<str:pk>/', DeleteList.as_view(), name='delete-list-api'),
    path('delete-task/<str:pk>/', DeleteTask.as_view(), name='delete-task-api'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

