from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View, generic

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class IndexView(View):
    def get(self, request, *args, **kwargs):
        all_tasks = Task.objects.all()

        context = {
            "task_list": all_tasks,

        }

        return render(request, "tasks/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class DeleteTagView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("task:tag-list")


class TaskChangeIsDone(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, id=pk)
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True

        task.save()

        return HttpResponseRedirect(reverse_lazy("task:index"))
