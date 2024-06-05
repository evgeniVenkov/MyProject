from django.contrib import messages
from django.shortcuts import render,redirect
from .form import UserForm, UserUpdateForm,ProfileImageForm
from django.contrib.auth.decorators import login_required

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


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST,request.FILES ,instance=request.user.profile)
        updateForm = UserUpdateForm(request.POST,instance=request.user)
        if profileForm.is_valid() and updateForm.is_valid():
            profileForm.save()
            updateForm.save()
            messages.success(request, 'Данные успешно изменены ')
            return redirect('profile')

    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateForm = UserUpdateForm(instance=request.user)

    data= {
        'profileForm':profileForm,
        'updateForm':updateForm,
    }


    return render(request,'users/profile.html',data)