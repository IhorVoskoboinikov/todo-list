from django.test import TestCase
from django.urls import reverse

from tasks.models import Task, Tag


class ModelsTest(TestCase):

    def setUp(self):
        for num in range(1, 11):
            Task.objects.create(content=f"Test content {num}")

        for id_ in range(1, 11, 2):
            update_task = Task.objects.get(id=id_)
            update_task.is_done = True
            update_task.save()

        self.test_tag = Tag.objects.create(name="Test tag")
        self.test_task = Task.objects.get(id=1)
        self.test_task.tags.add(self.test_tag)

    def test_teg_str(self):
        self.assertEqual(str(self.test_tag), self.test_tag.name)

    def test_task_str(self):
        self.assertEqual(str(self.test_task), self.test_task.content)

    def test_ordering_task(self):
        response = self.client.get(reverse("task:index"))
        self.assertEqual(response.status_code, 200)
        tasks_from_context = list(response.context["task_list"])
        sorted_tasks = list(Task.objects.all())
        self.assertEqual(tasks_from_context, sorted_tasks)
