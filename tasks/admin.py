from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "create_at", "deadline", "is_done"]
    search_fields = ("content",)
    list_filter = ("is_done",)


admin.site.register(Tag)
