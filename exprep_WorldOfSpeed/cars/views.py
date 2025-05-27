from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CarCreateForm, CarEditForm, CarDeleteForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from exprep_WorldOfSpeed.utils import  get_user_obj
from .models import Car
# Create your views here.

class CarCreateView(CreateView):
    template_name = 'cars/car-create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)

class CatalogueView(ListView):
    template_name = 'cars/catalogue.html'

    def get_queryset(self):
        user = get_user_obj()
        cars = user.cars.all()
        return cars

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = get_user_obj()
        context['cars'] = user.cars.all()
        return context

class CarDetailsView(DetailView):
    template_name = 'cars/car-details.html'
    model = Car


class CarEditView(UpdateView):
    template_name = 'cars/car-edit.html'
    model = Car
    form_class = CarEditForm
    success_url = reverse_lazy('catalogue')

class CarDeleteView(DeleteView):
    template_name = 'cars/car-delete.html'
    model = Car
    form_class = CarDeleteForm
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
