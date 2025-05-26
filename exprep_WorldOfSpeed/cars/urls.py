from django.urls import path
from . import views

urlpatterns = [
    path('create',views.CarCreateView.as_view(),name='car-create'),
]