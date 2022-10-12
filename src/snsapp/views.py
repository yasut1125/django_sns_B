from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Post, Connection


class Home(ListView):
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        return Post.objects.all()
    
   
class MyPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
            context = super().get_context_data(*args, **kwargs)
            context['connection'] = Connection.objects.get_or_create(user=self.request.user)
            return context

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['content']
    success_url = reverse_lazy('mypost')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('mypost')

    def test_func(self, **kwargs):
        pk = self.kwargs["pk"]
        print(pk)
        post = Post.objects.get(pk=pk)
        return (post.user == self.request.user)