from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='recipe-create'),

]
