from django.shortcuts import render
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileCreateForm
from django.urls import reverse_lazy
# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('home')
