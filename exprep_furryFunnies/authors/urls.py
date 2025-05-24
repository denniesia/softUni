from django.urls import path
from . import views

urlpatterns = [
    path('create-author', views.AuthorCreateView.as_view(), name='create-author'),

]
