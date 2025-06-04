from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

UserModel = get_user_model()

class CustomUserCreationForm(auth_forms.UserCreationForm):
    age = forms.IntegerField()
    #other fields of 'Profile'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        # fields = auth_forms.UserCreationForm.Meta.fields + ('age',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
            age=self.cleaned_data['age'],
        )
        if commit:
            profile.save()
        return user

