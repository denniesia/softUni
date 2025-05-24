from django.urls import path
from . import views

urlpatterns = [
    path('create', views.AuthorCreateView.as_view(), name='create-author'),
    path('details', views.AuthorDetailsView.as_view(), name='details-author'),
]
