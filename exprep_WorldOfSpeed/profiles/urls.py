from django.urls import path
from . import views

urlpatterns = [
    path('create',views.CreateProfileView.as_view(), name='profile-create' ),
    path('details',views.ProfileDetailsView.as_view(), name='profile-details' ),
]