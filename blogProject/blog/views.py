# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# from django.http import HttpResponse
# Create your views here.

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'BLog Post 1',
#         'content': 'First post content',
#         'date_posted': 'July 23, 2020'
#     },
#      {
#         'author': 'Jane Doe',
#         'title': 'BLog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'July 22, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)



class PostListView(ListView):
    model = Post  
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post  
    template_name = 'blog/user_post.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5  

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post  

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:     
            return True
        return False  


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post 
    success_url = '/blog/blog'          

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:     
            return True
        return False 

def about(request):    
    return render(request, 'blog/about.html', {'title':'About'})

# blog -> templates -> blog -> templates.html   

