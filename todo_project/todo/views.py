from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Lista e cria tarefas (somente do usuário logado)
@login_required(login_url='login')
def index(request):
    # filtra apenas as tasks do usuário
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user        # atribui o usuário que criou a tarefa
            task.save()
            return redirect('/')            # redireciona após criar

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


# Atualizar tarefa — garante que a task pertença ao usuário
@login_required(login_url='login')
def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update.html', context)


# Deletar tarefa — também verifica propriedade
@login_required(login_url='login')
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task': task}
    return render(request, 'delete.html', context)
