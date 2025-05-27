from django import forms
from .models import  Car
from exprep_WorldOfSpeed.utils import get_user_obj

class CarBaseForm(forms.ModelForm):
    pass

class CarCreateForm(CarBaseForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']

        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),

        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        return year


class CarEditForm(CarBaseForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']