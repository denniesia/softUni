from django.shortcuts import render
from django import forms
from .models import  Post
from .forms import  PostCreateForm, PostEditForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from exprep_furryFunnies.utils import get_user_obj
# Create your views here.

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)

class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/details-post.html'


class PostEditView(UpdateView):
    model = Post
    pk_url_kwarg = 'id'
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')