from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'this username already exist')
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'this email already exist')
                return redirect('register/')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
            return redirect('login')

        else:
            messages.info(request, 'This password not matching')
            return redirect('register/')

    return render(request, 'Register/Register.html')


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home/')

        else:
            messages.info(request, 'please provide correct details')
            return redirect('login')

    return render(request, 'Register/Login.html')


def log_out(request):
    auth.logout(request)
    return redirect('login')


def home_page(request):

    return render(request, 'Register/home.html')


def index_detail(request):

    return render(request, 'movie/index.html')


def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        user.username=username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password
        user.password1 = password1

        user.save()

        return redirect('http://127.0.0.1:8000/home/')

    return render(request,'Register/update.html')


def detail_user(request,user_id):
    user=User.objects.get(id=user_id)

    return render(request,'Register/details.html',{'user': user})


def list_user(request):
    user=User.objects.all()

    return render(request,'Register/userlist.html',{'user': user})


def admin_home(request):

    return render(request, 'admin/adminhome.html')
