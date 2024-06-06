from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserForm, ProfileForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if  request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Аккаунт: {username} успешно создан!')
            return redirect('main')

    else:
        form = UserForm()


    return render(request, 'users/register.html',{'form':form})



@login_required()
def profile_view(request):
    if request.method == "POST":
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        updateform = UserUpdateForm(request.POST, instance=request.user)
        if profileform.is_valid() and updateform.is_valid():
            profileform.save()
            updateform.save()
            messages.success(request,'Данные успешно изменены')
            return redirect ('profile')
    else:
        profileform = ProfileForm(instance=request.user.profile)
        updateform = UserUpdateForm(instance=request.user)

    data = {'profileform':profileform, 'updateform':updateform}

    return render(request, "users/profile.html",data)

# Create your views here.
