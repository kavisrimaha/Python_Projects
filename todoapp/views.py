from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm





# Create your views here.
#login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todoapp:task_list')  # redirect after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('todoapp:login')
    return render(request, 'todoapp/login.html')

#logout 
def user_logout(request):
    logout(request)
    return redirect('todoapp:login')
#signup
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('todoapp:task_list') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'todoapp/signup.html', {'form': form})

# read(view the list)
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    total = tasks.count()
    completed = tasks.filter(status=True).count()
    pending = total - completed
    return render(request, 'todoapp/task_list.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending
    })

# create new list
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save yet
            task.user = request.user        # Assign logged-in user
            task.save()
            return redirect('todoapp:task_list')
    else:
        form = TaskForm()
    return render(request, 'todoapp/task_form.html', {'form': form})
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todoapp:task_list') 
    else:
        form = TaskForm(instance=task)

    return render(request, 'todoapp/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # <- raises 404 if not found
    if request.method == 'POST':
        task.delete()
        return redirect('todoapp:task_list')
    return render(request, 'todoapp/task_confirm_delete.html', {'task': task})