from django.shortcuts import render, HttpResponse, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def addtask(request):
    queryset = Task.objects.all()
    form = TaskForm()
    context = {"tasks": queryset, "form": form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    return render(request, "tasks/lists.html", context)


def updatetask(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"form": form, "task": task}
    return render(request, "tasks/update.html", context)


def deletetask(request, pk):
    task = Task.objects.get(pk=pk)
    context = {"task": task}
    task.delete()
    return redirect("tasks")
