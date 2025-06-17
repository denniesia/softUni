from django.urls import path, include
from . import views
urlpatterns = [
    path('create/',views.ProfileCreateView.as_view() , name='profile-create' ),
    path('<int:pk>/', include([
        path('details/', views.ProfileDetailsView.as_view() , name='profile-details' ),
    ]))
]
