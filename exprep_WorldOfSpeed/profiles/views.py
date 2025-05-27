from django.shortcuts import render
from django.views.generic import  CreateView, DetailView, UpdateView, DeleteView
from .forms import ProfileCreateForm
from django.urls import reverse_lazy
from exprep_WorldOfSpeed.utils import get_user_obj
from .models import Profile
# Create your views here.
class CreateProfileView(CreateView):
    template_name = 'profiles/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')

class ProfileDetailsView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        total_all_cars = self.object.cars.all()
        total_sum = sum(car.price for car in total_all_cars )
        context['total_sum'] = total_sum
        return context