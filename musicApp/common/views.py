from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from albums.models import Album
from profiles.forms import ProfileCreateForm
from django.urls import reverse_lazy

from musicApp.utils import get_user_obj

# Create your views here.
class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')


    def get_template_names(self):
        profile = get_user_obj() #None or QuerySet
        if profile:
            return ['profiles/home-with-profile.html']
        else:
            return ['profiles/home-no-profile.html']
