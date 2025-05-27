from django.urls import path, include
from . import views

urlpatterns = [
    path('create',views.CarCreateView.as_view(),name='car-create'),
    path('catalogue', views.CatalogueView.as_view(), name='catalogue'),
    path('<int:pk>', include([
        path('/details', views.CarDetailsView.as_view(), name = 'car-detail'),
        path('/edit', views.CarEditView.as_view(), name = 'car-edit'),
        path('/delete', views.CarDeleteView.as_view(), name = 'car-delete'),
    ]))


]