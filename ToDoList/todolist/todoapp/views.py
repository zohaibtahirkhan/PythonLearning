from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import List, Task
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
class GetListsView(ListView):
    model = List
    template_name = 'homepage.html'
    context_object_name = 'lists'
    paginate_by = 8

# Class-based view
# class ListDetailView(DetailView):
#     model = List
#     template_name = 'detailed-list.html'
#     context_object_name = 'list'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = Task.objects.filter(list=self.object)
#         return context


# Function-based view
@login_required
def getTasks(request, pk):
    my_list = List.objects.get(id=pk)
    if my_list.creator == request.user:
        tasks = my_list.task_set.all()
        return render(request, 'detailed-list.html', context={'list': my_list, "tasks": tasks})
    else:
        return redirect('warning')


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    fields = ['name']
    template_name = 'list-form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'objective']
    template_name = 'task-form.html'

    def form_valid(self, form):
        list_obj = List.objects.get(id=self.kwargs['list_id'])
        form.instance.list = list_obj
        return super().form_valid(form)


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['name']
    template_name = 'list-form.html'


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = 'list_confirm_delete.html'
    success_url = reverse_lazy("homepage")


@login_required
def markAsComplete(request, pk):
    obj = List.objects.get(id=pk)
    if request.user == obj.creator:
        obj.complete = True
        obj.save()
        return redirect('homepage')
    else:
        return redirect('warning')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'objective']
    template_name = 'task-form.html'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task-confirm-delete.html'

    def get_success_url(self):
        return reverse_lazy('tasks', kwargs={'pk': self.object.list.id})


@login_required
def markTaskAsComplete(request, pk):
    obj = Task.objects.get(id=pk)
    if obj.list.creator == request.user:
        obj.done = True
        obj.save()
        return redirect('tasks', obj.list.id)
    else:
        return redirect('warning')
