from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .form import UserForm, ProfileForm,UserUpdateForm,PostsForm,PochtaForm
from django.contrib.auth.decorators import login_required
from .models import Posts,Pochta
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail

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

# def post_view(request):
#     data={'posts':Posts.objects.all()}
#     return render(request, 'users/posts.html',data)
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
class ShowPosts(ListView):
    model = Posts
    template_name = 'users/posts.html'
    context_object_name = 'posts'
    ordering = ['date']
    paginate_by = 4

    # передача доп параметров
    def get_context_data(self,**kwards):
        ctx = super(ShowPosts,self).get_context_data(**kwards)
        ctx['name'] = f'{self.request.user.username}'

        return ctx
class ShowPostsUser(ListView):
    model = Posts
    template_name = 'users/user_posts.html'
    context_object_name = 'posts'

    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Posts.objects.filter(avtor=user).order_by('-date')
    def get_context_data(self,**kwards):
        ctx = super(ShowPostsUser,self).get_context_data(**kwards)
        ctx['title'] = f'Статьи: {self.kwargs.get('username')}'

        return ctx
class DetailPosts(DetailView):
    model = Posts
    # template_name = 'users/posts_detail.html'
    context_object_name = 'post'
    def get_context_data(self,**kwards):
        ctx = super(DetailPosts,self).get_context_data(**kwards)
        ctx['title'] = Posts.objects.get(pk=self.kwargs['pk']).title

        return ctx

class CreatePosts(CreateView,LoginRequiredMixin):
    model = Posts
    template_name = 'users/create_posts.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self,**kwards):
        ctx = super(CreatePosts,self).get_context_data(**kwards)
        ctx['title'] = 'Добавить статью'
        ctx['btn_text'] = "Добавить"
        return ctx

class UpdatePosts(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model = Posts
    template_name = 'users/create_posts.html'
    fields = ['title','content']

    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.avtor:
            return True
        return False
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self,**kwards):
        ctx = super(UpdatePosts,self).get_context_data(**kwards)

        ctx['title'] = Posts.objects.get(pk=self.kwargs['pk'])
        ctx['btn_text'] = 'Обновить'
        return ctx

class DeletePost(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Posts
    success_url = '/'
    template_name = 'users/delete_post.html'

    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.avtor:
            return True
        return False

class Pochta(CreateView):
    model= Pochta
    template_name = 'users/contakti.html'
    fields = ['tema', 'mail','text']

    def form_valid(self, form):
        subject = form.cleaned_data['tema']
        plain_message = form.cleaned_data['text']
        from_email = form.cleaned_data['mail']
        to = 'venigret90@mail.ru'
        send_mail(subject, plain_message, from_email, [to])

        return super().form_valid(form)