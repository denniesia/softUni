from django import forms
from .models import Author

class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorCreateForm(AuthorBaseForm):
    pass