from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    succes_url = reverse_lazy('home')