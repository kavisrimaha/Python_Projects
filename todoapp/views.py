from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, DailyRoutine, RoutineCompletion, Note
from .forms import TaskForm, DailyRoutineForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.utils import timezone


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
    routine_count = DailyRoutine.objects.filter(user=request.user).count()
    note_count = Note.objects.filter(user=request.user).count()
    return render(request, 'todoapp/task_list.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending,
        'routine_count': routine_count,
        'note_count': note_count
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

# --- Daily Routine Views ---

@login_required
def routine_list(request):
    routines = DailyRoutine.objects.filter(user=request.user).order_by('-id')
    today = timezone.now().date()
    
    # Get completions for today
    today_completions = RoutineCompletion.objects.filter(
        routine__user=request.user,
        date=today,
        completed=True
    ).values_list('routine_id', flat=True)
    
    return render(request, 'todoapp/routine_list.html', {
        'routines': routines,
        'today_completions': today_completions,
        'today': today
    })

@login_required
def routine_create(request):
    if request.method == 'POST':
        form = DailyRoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.user = request.user
            routine.save()
            return redirect('todoapp:routine_list')
    else:
        form = DailyRoutineForm()
    return render(request, 'todoapp/task_form.html', {'form': form, 'title': 'Add Daily Routine'})

@login_required
def routine_delete(request, pk):
    routine = get_object_or_404(DailyRoutine, pk=pk, user=request.user)
    if request.method == 'POST':
        routine.delete()
        return redirect('todoapp:routine_list')
    return render(request, 'todoapp/task_confirm_delete.html', {'task': routine, 'is_routine': True})

@login_required
def routine_toggle(request, pk):
    routine = get_object_or_404(DailyRoutine, pk=pk, user=request.user)
    today = timezone.now().date()
    completion, created = RoutineCompletion.objects.get_or_create(
        routine=routine,
        date=today
    )
    completion.completed = not completion.completed
    completion.save()
    return redirect('todoapp:routine_list')

# --- Note Views ---

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'todoapp/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('todoapp:note_list')
    else:
        form = NoteForm()
    return render(request, 'todoapp/note_form.html', {'form': form, 'title': 'Create Note'})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('todoapp:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'todoapp/note_form.html', {'form': form, 'title': 'Edit Note'})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('todoapp:note_list')
    return render(request, 'todoapp/task_confirm_delete.html', {'task': note, 'is_note': True})