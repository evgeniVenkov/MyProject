from django.shortcuts import render


def register_view(request):
    return render(request, 'users/register.html')

def login_view(request):
    return render(request, 'users/login.html')

def exit_view(request):
    return render(request, 'user/exit.html')

def profile_view(request):
    return render(request, "users/profile.html")

# Create your views here.
