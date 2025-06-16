from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),

]
