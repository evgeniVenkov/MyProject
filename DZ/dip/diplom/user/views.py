from django.shortcuts import render
from.form import profileForm,UserForm,linksForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import links
def index(request):
    return render(request, 'user/home.html')

@login_required()
def profile_view(request):
    if request.method == "POST":
        profileform = profileForm(request.POST,instance=request.user)

        if profileform.is_valid():
            profileform.save()
            return redirect ('profile')
    else:
        profileform = profileForm(instance=request.user)


    data = {'profileform':profileform}

    return render(request, "user/profile.html",data)
def register_view(request):
    if  request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = UserForm()

    return render(request, 'user/register.html',{'form':form})

def links_view(request):
    if request.method == "POST":
        f1 = request.POST.copy()
        f1['user'] = request.user
        form = linksForm(f1)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('link')
    else:
        form = linksForm()


    alllinks = links.objects.filter(user=request.user)
    data = {'form':form,'alllinks':alllinks}
    return render(request,'user/links.html',data)
# Create your views here.


def about_view(request):
    return render(request, 'user/about.html')