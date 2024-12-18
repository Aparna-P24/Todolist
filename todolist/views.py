from django.shortcuts import render, redirect
from todolist.models import Tasklist
from todolist.forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request, ("New task added for today to complete!!!"))
        return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 8)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def delete_element(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
        messages.success(request, ("selected task is deleted successfully!"))
    else:
        messages.error(request, ("Status cannot be changed"))
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Succesfully edited!!"))
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Status cannot be changed"))
    return redirect('todolist')


def pending_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


@login_required
def activity(request):
    context = {
        "activity_text": 'Hi! This is the home page of daily activities app'}
    return render(request, 'dailyactivities.html', context)


@login_required
def contactus(request):
    context = {"contactus_text": 'Hi! This is the home page of contact us app'}
    return render(request, 'contactus.html', context)


def index(request):
    context = {"Index_text": 'Hi! This is the Index page of contact us app'}
    return render(request, 'index.html', context)
