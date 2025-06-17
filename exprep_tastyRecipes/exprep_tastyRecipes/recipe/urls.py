from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('<int:pk>/', include([
        path('details/', views.RecipeDetailsView.as_view(), name='recipe-details'),
        path('edit/', views.RecipeEditView.as_view(), name='recipe-edit'),
        path('delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    ])),

]
