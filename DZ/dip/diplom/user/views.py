from django.shortcuts import render
from.form import profileForm
from django.shortcuts import redirect
def index(request):
    return render(request, 'user/home.html')


def profile_view(request):
    if request.method == "POST":
        profileform = profileForm(request.POST, request.FILES, instance=request.user.profile)

        if profileform.is_valid():
            profileform.save()
            return redirect ('profile')
    else:
        profileform = profileForm(instance=request.user.profile)

    data = {'profileform':profileform,}

    return render(request, "user/profile.html",data)
# Create your views here.
