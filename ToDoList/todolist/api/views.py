from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from todoapp.models import List, Task
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ListSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated


# Create APIs
class CreateList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        list = List.objects.create(
            name=request.data['name'],
            creator=request.user)
        serializer = ListSerializer(list, many=False)
        return Response(serializer.data)


class CreateTask(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        my_list = get_object_or_404(List, id=request.data['list'])
        task = Task.objects.create(
            title=request.data['title'],
            objective=request.data['objective'],
            list=my_list)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)


# Retrieve APIs
class ListLists(APIView):
    def get(self, request, *args, **kwargs):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)


class ListTasks(APIView):
    def get(self, request, *args, **kwargs):
        list = List.objects.get(id=kwargs["pk"])
        tasks = list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


# Update APIs
class UpdateList(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        list = List.objects.get(id=kwargs["pk"])
        list.name = request.data['name']
        list.save()
        serializer = ListSerializer(list, many=False)
        return Response(serializer.data)


class UpdateTask(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])
        task.title = request.data['title']
        task.objective = request.data['objective']
        task.save()
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)


# Delete APIs
class DeleteList(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        list = List.objects.get(id=kwargs["pk"])
        serializer = ListSerializer(list, many=False)
        list.delete()
        return Response(serializer.data)


class DeleteTask(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])
        serializer = TaskSerializer(task, many=False)
        task.delete()
        return Response(serializer.data)

