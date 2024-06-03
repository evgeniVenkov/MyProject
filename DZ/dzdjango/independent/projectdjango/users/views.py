from django.contrib import messages
from django.shortcuts import render,redirect
from .form import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'Account created for ' + username)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'users/register.html',{'form': form})