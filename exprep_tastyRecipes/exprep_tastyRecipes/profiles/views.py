from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Profile
from .forms import ProfileCreateForm, ProfileDetailsForm, ProfileEditForm
from django.urls import reverse_lazy
# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    form_class = ProfileDetailsForm
    template_name = 'profiles/details-profile.html'

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'