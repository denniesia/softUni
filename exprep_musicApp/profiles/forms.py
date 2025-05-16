from django import forms
from .models import Profile
from exprep_musicApp.mixins import PlaceholderMixin

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(PlaceholderMixin, ProfileBaseForm):
    pass
