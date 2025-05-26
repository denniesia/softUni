from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CarCreateForm
from django.views.generic import CreateView
from exprep_WorldOfSpeed.utils import  get_user_obj
# Create your views here.

class CarCreateView(CreateView):
    template_name = 'cars/car-create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)