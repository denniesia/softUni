from django.shortcuts import render
from django.views.generic import CreateView
from .models import Recipe
from django.urls import reverse_lazy
from .forms import RecipeCreateForm

from exprep_tastyRecipes.utils import get_user_obj
# Create your views here.
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)