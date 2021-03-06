from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.utils import TaskMixin, TaskFilter


class TaskView(View):
    """View that collects all data concerning the chosen task
    and then renders a card with task info."""

    def get(self, request, pk):
        task_selected = (
            Task.objects.select_related("executor", "status", "author")
            .prefetch_related("labels")
            .get(pk=pk)
        )
        return render(request, "task-detail.html", {"task": task_selected})


class Tasks(LoginRequiredMixin, View):
    """View that shows list of tasks. Allows filtration through GET params.
    Full list of tasks is shown by default."""

    def get(self, request):
        tasks = Task.objects.select_related("executor", "status", "author").all()
        tasks = TaskFilter._filter(self, request, tasks)
        labels = Label.objects.all()
        statuses = Status.objects.all()
        users = User.objects.all()

        return render(
            request,
            "task-list.html",
            {"tasks": tasks, "users": users, "statuses": statuses, "labels": labels},
        )


class TaskCreate(LoginRequiredMixin,
                 SuccessMessageMixin,
                 TaskMixin,
                 CreateView):
    template_name = "task-create.html"
    success_message = "Задача успешно создана"


class TaskUpdate(LoginRequiredMixin,
                 SuccessMessageMixin,
                 TaskMixin,
                 UpdateView):
    template_name = "task-update.html"
    success_message = "Задача успешно изменена"


class TaskDelete(LoginRequiredMixin,
                 SuccessMessageMixin,
                 TaskMixin,
                 DeleteView):
    template_name = "task-delete.html"
    success_message = "Задача успешно удалена"

    def get(self, request, pk):
        self.object = self.get_object()
        if self.object.author.pk == request.user.pk:
            return render(request, "task-delete.html", {'task': self.object})
        else:
            messages.error(request, "Задачу может удалить только её автор")
            return redirect(reverse('tasks'))
