from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from .models import ExtendedUser


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            phone_number = request.POST['phone_number']
            gender = request.POST['gender']
            user = User.objects.create_user(first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'],
                                            email=request.POST['email'],
                                            username=request.POST['username'],
                                            password=request.POST['password1'])
            ExtendedUser(phone_number=phone_number, gender=gender, user=user).save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})


def show(request):
    data = ExtendedUser.objects.all()
    return render(request, 'show.html', {'data': data})
