from django.shortcuts import render
from django.http import HttpResponse
from .models import Nariai
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .forms import CreatePostForm

'''
def home(request):
    return HttpResponse('Labas, django!')
'''
'''
def home(request):
    return render(request, 'index2.html')
'''

class PostListView(ListView):
    model = Nariai
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Nariai.objects.all()
        return context

class PostCreateView(CreateView):
    model = Nariai
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = '/'

class PostDeleteView(DeleteView):
    model = Nariai
    template_name = 'delete_post.html'
    success_url = '/'

