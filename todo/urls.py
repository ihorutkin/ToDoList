from django.urls import path

from todo.views import (
    TodoListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_complete_task
)


urlpatterns = [
    path("", TodoListView.as_view(), name="home_page"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:pk>", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag_delete"),
    path("tags/toggle_complete/<int:pk>", toggle_complete_task, name="task_toggle"),
]

app_name = "todo"
