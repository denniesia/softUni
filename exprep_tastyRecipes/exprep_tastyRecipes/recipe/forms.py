from django import forms
from .models import Recipe

class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)


class RecipeCreateForm(RecipeBaseForm):
    title = forms.CharField(
        error_messages={'unique': "We already have a recipe with the same title!" },
    )
