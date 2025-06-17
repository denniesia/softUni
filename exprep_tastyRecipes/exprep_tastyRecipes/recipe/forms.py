from django import forms
from .models import Recipe

class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)


class RecipeCreateForm(RecipeBaseForm):
    class Meta(RecipeBaseForm.Meta):
        title = forms.CharField(
            error_messages={'unique': "We already have a recipe with the same title!" },
        )

        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space!',
            'cooking_time': 'Provide the cooking time in minutes',
        }
