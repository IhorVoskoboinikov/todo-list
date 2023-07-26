from django import forms
from .models import Task, Tag


class BaseTaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'}
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TaskCreateForm(BaseTaskForm):
    pass


class TaskUpdateForm(BaseTaskForm):
    class Meta(BaseTaskForm.Meta):
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
