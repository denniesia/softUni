from django import forms
from profiles.models import Profile

class ProfileBaseForm(forms.ModelForm):
    pass

class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('username', 'email','age', 'password')

        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }

