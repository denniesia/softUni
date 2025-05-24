from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Author
from .forms import AuthorCreateForm, AuthorEditForm
from django.urls import reverse_lazy
from exprep_furryFunnies.utils import get_user_obj
# Create your views here.
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorDetailsView(DetailView):
    template_name = 'authors/details-author.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        author = self.get_object()
        last_post = author.posts.last()
        context['last_post'] = last_post
        return context

    def get_object(self, queryset=None):
        return get_user_obj()

class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_user_obj()

class AuthorDeleteView(DeleteView):
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()