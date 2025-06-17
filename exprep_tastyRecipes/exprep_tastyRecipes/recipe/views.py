from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Recipe
from django.urls import reverse_lazy
from .forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm

from exprep_tastyRecipes.utils import get_user_obj
# Create your views here.
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('catalogue')
    
    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)

class CatalogueView(ListView):
    template_name = 'recipe/catalogue.html'

    def get_queryset(self):
        queryset = Recipe.objects.all()
        return queryset

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipe/details-recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredients_str = self.object.ingredients  # Example: "cheese, milk, eggs"
        context['ingredients'] = [ingredient.strip() for ingredient in ingredients_str.split(', ')]
        return context

class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = 'recipe/edit-recipe.html'
    success_url = reverse_lazy('catalogue')


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe/delete-recipe.html'
    form_class = RecipeDeleteForm
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)