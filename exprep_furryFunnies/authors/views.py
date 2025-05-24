from django.shortcuts import render
from django.views.generic import CreateView
from .models import Author
from .forms import AuthorCreateForm
# Create your views here.
class AuthorCreateView(CreateView):
    pass
    # model = Author
    # form_class = AuthorCreateForm
    # template_name = 'authors/create-author.html'
    # success_url = 'dashboard'