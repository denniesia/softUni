from django import forms
from .models import Profile

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef', 'bio']


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['bio',]

class ProfileDetailsForm(ProfileBaseForm):
    pass

class ProfileEditForm(ProfileBaseForm):
    pass



