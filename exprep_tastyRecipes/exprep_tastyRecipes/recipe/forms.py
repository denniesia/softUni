from django import forms
from .models import Recipe
from exprep_tastyRecipes.mixins import ReadOnlyMixin

class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)

        title = forms.CharField(
            error_messages={'unique': "We already have a recipe with the same title!"},
        )

        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space!',
            'cooking_time': 'Provide the cooking time in minutes',
        }


class RecipeCreateForm(RecipeBaseForm):
    pass

class RecipeEditForm(RecipeBaseForm):
    pass

class RecipeDeleteForm(ReadOnlyMixin,RecipeBaseForm):
    readonly_fields = ('title','cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url')