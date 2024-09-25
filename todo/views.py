from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    template_name = "todo/todo_list.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:home_page")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:home_page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/tag_delete_confirm.html"
    success_url = reverse_lazy("todo:home_page")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_delete_confirm.html"
    success_url = reverse_lazy("todo:tag_list")


def toggle_complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:home_page")
