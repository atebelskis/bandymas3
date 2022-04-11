from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .forms import CreatePostForm, PostUpdateForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


'''
def home(request):
    return HttpResponse('Labas, django!')
'''
'''
def home(request):
    return render(request, 'index2.html')
'''

class PostListView(ListView):
    model = Post
    paginate_by = 4  # kiek irasu puslapyje
    template_name = 'index2.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    login_url = '/login/'
    template_name = 'create_post.html'
    success_url = '/'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'delete_post.html'
    login_url = '/login/'
    success_url = '/'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    login_url = '/login/'
    #fields = '__all__'
    template_name = 'update_post.html'
    success_url = '/'

def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html', {})

def log_out(request):
    logout(request)
    return redirect('login')





