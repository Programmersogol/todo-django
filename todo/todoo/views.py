from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import ToDo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ToDo



# ---------- SIGNUP ----------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('frm')
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, "singup.html")


# ---------- LOGIN ----------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('frm')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('todo')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


# ---------- LOGOUT ----------
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')


# ---------- TODO LIST ----------
@login_required
def todo_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority', 'medium')
        if title:
            ToDo.objects.create(title=title, priority=priority, user=request.user)
            messages.success(request, "Task added successfully!")
            return redirect('todo')

    result = ToDo.objects.filter(user=request.user).order_by('-date')
    return render(request, "todo.html", {'res': result})


# ---------- EDIT TODO ----------
@login_required(login_url='login')
def edit_todo_view(request, srno):
    todo = get_object_or_404(ToDo, srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        todo.title = title
        todo.save()
        messages.success(request, "Task updated successfully!")
        return redirect('todo')

    return render(request, 'edit_todo.html', {'obj': todo})


# ---------- DELETE TODO ----------
@login_required(login_url='login')
def delete_todo_view(request, srno):
    todo = get_object_or_404(ToDo, srno=srno, user=request.user)
    todo.delete()
    messages.success(request, "Task deleted successfully.")
    return redirect('todo')


@login_required(login_url='/login')
@csrf_exempt
def edit_todo_ajax(request, srno):
    if request.method == "POST":
        title = request.POST.get('title')
        try:
            obj = ToDo.objects.get(srno=srno, user=request.user)
            obj.title = title
            obj.save()
            return JsonResponse({'status': 'success', 'title': obj.title})
        except ToDo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required(login_url='/login')
@csrf_exempt
def delete_todo_ajax(request, srno):
    if request.method == "POST":
        try:
            task = ToDo.objects.get(srno=srno, user=request.user)
            task.delete()
            return JsonResponse({'status': 'success'})
        except ToDo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@login_required(login_url='/login')
@csrf_exempt
def toggle_done(request, srno):
    if request.method == "POST":
        try:
            task = ToDo.objects.get(srno=srno, user=request.user)
            task.is_done = not task.is_done
            task.save()
            return JsonResponse({'status': 'success', 'is_done': task.is_done})
        except ToDo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

