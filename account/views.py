from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, Authenticate, UserUpdateForm


@login_required(login_url='login')
def account(request):
    if request.user.is_authenticated:
        error = ''
        form = UserUpdateForm(instance=request.user)

        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                return redirect('account_home')
            else:
                error = 'Неправильно введенные данные'

        data = {
            'form': form,
            'error': error
        }
        return render(request, 'account/account.html', data)
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
                    return redirect('account_home')
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
