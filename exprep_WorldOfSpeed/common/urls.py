from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', include('profiles.urls')),
    path('car/', include('cars.urls')),

]