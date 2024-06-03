from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
            # form.save()
    return render(request, 'users/register.html')