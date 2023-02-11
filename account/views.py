from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, Authenticate, CreateLink
from .models import Links


@login_required(login_url='login')
def account(request):
    if request.user.is_authenticated:
        return render(request, 'account/account.html')
    else:
        return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('account_home')
    else:
        error = ''
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('account_home')
            else:
                error = 'Неправильно введенные данные'

        data = {
            'form': form,
            'error': error
        }
        return render(request, 'registration/register.html', data)


def login_acc(request):
    if request.user.is_authenticated:
        return redirect('account_home')
    else:
        error = ''
        form = Authenticate()
        if request.method == 'POST':
            form = Authenticate(data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                error = 'Неправильно введенные данные'
        data = {
            'form': form,
            'error': error,
        }
    return render(request, 'registration/login.html', data)


@login_required(login_url='login')
def logout_acc(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')


@login_required(login_url='login')
def links(request):
    if request.user.is_authenticated:
        error = ''
        form = CreateLink()
        if request.method == 'POST':
            form = CreateLink(data=request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
            else:
                error = 'Неправильно введенные данные'

        link = Links.objects.all()
        data = {
            'form': form,
            'link': link,
            'error': error
        }
        return render(request, 'account/links.html', data)
    else:
        return redirect('login')
