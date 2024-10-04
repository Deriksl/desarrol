
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Task
from .forms import taskform
from .models import Country, State
from .forms import CountryForm, StateForm

def home(request):
    return render(request, 'home.html')

def task(request):
    tasks = Task.objects.all()  
    return render(request, 'task.html', {'tasks': tasks})

def addtask(request):
    if request.method == 'GET':
        return render(request, 'addtask.html', {
            'form': taskform()
        })
    else:
        try:
            form = taskform(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except:
            return render(request, 'addtask.html', {
                'form': taskform(),
                'error': 'Hubo un error en la información'
            })

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and not password2:
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'error': 'Debes de confirmar tu contraseña'
            })
        elif password1 != password2:
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden'
            })
        else:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=password1
                )
                user.save()
                login(request, user)
                return redirect('task')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'El usuario ya existe'
                })


def signgin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario y contraseña no coinciden'
            })
        else:
            login(request, user)
            return redirect('task')

def signout(request):
    logout(request)
    return redirect('home')

def updatetasks(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_list = Task.objects.all()

    if request.method == 'GET':
        form = taskform(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form,
            'task_list': task_list
        })
    else:
        form = taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task')  
        else:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'task_list': task_list,
                'error': 'Error actualizando la tarea'
            })
        
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  
    return render(request, 'task_detail.html', {
        'task': task
    })



def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})


def add_country(request):
    if request.method == 'GET':
        form = CountryForm()
        return render(request, 'add_country.html', {'form': form})
    else:
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('countries')

def states(request):
    states = State.objects.all()
    return render(request, 'states.html', {'states': states})


def add_state(request):
    if request.method == 'GET':
        form = StateForm()
        return render(request, 'add_state.html', {'form': form})
    else:
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('states')
        

def list_countries(request):
    countries = Country.objects.all()
    return render(request, 'list_countries.html', {'countries': countries})

def list_states(request):
    states = State.objects.all()
    return render(request, 'list_states.html', {'states': states})

def update_country(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('list_countries')
    else:
        form = CountryForm(instance=country)
    return render(request, 'update_country.html', {'form': form})

def update_states(request, pk):
    state = get_object_or_404(State, pk=pk)
    form = StateForm(request.POST or None, instance=state)
    if form.is_valid():
        form.save()
        return redirect('list_states')  # Cambia 'url_name' por la URL a la que quieras redirigir.
    return render(request, 'update_states.html', {'form': form})