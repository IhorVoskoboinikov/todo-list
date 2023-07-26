from django.urls import path

from .views import (
    IndexView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,

    TagListView,
    TagCreateView,
    TagUpdateView,
    DeleteTagView,
    TaskChangeIsDone,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/is_done", TaskChangeIsDone.as_view(), name="task-done"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/", DeleteTagView.as_view(), name="tag-delete"),

]

app_name = "task"
