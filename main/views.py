from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import TaskForm
from django.urls import reverse_lazy
from datetime import date,datetime,timedelta

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

    

class TaskDetailView(DetailView):
    model = Post
    template_name = 'task_detail.html'
    



class TaskCreateView(CreateView):
    model = Post
    template_name = 'task_create.html'
    form_class = TaskForm
    

class TaskUpdateView(UpdateView):
    model = Post
    template_name = 'task_create.html'
    form_class = TaskForm

class TaskDeleteView(DeleteView):
    model = Post
    template_name = 'task_delete.html'
    success_url = reverse_lazy('home')