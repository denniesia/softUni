from django.shortcuts import render
from django.views.generic import CreateView
from .models import Author
from .forms import AuthorCreateForm
from django.urls import reverse_lazy
# Create your views here.
class AuthorCreateView(CreateView):

    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')