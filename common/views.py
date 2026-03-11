from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_login = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=user_login, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/user/' + str(user.id) + '/')
        else:
            return render(request, 'login.html', context={'error': 'Invalid login or password'})

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user_login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_user(username=user_login,
    email=email,
    password=password,
    first_name=first_name,
    last_name=last_name)
        user.save()
        return redirect('login')
    else:
        return render(request,'register.html')

def logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user_groups = user.groups.all()[0]
    return render(request, 'user_page.html', context={'user': user, 'group_name': user_groups.name})