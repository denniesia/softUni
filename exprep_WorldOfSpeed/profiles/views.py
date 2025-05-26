from django.shortcuts import render
from django.views.generic import  CreateView, DetailView, UpdateView, DeleteView
from .forms import ProfileCreateForm
from django.urls import reverse_lazy
# Create your views here.
class CreateProfileView(CreateView):
    template_name = 'profiles/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')