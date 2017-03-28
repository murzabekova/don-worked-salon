from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                context = {'log_error': 'Пользователь не найден'}
        context = {'log_error': 'Логин или пароль не правильны'}
    return render(request, 'accounts/login.html', context)
