# Generated by Django 4.1 on 2023-07-26 08:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={
                "ordering": ["name"],
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
            },
        ),
        migrations.AlterModelOptions(
            name="task",
            options={
                "ordering": ["-create_at"],
                "verbose_name": "task",
                "verbose_name_plural": "tasks",
            },
        ),
    ]
