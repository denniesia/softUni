from django import forms
from .models import Profile

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ['nickname', 'first_name', 'last_name', 'chef']

