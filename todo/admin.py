from django.contrib import admin
from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("is_done", "-created_time",)
    list_display = [
        "content",
        "created_time",
        "deadline_time",
        "is_done",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ("name",)
    list_display = ["name"]
