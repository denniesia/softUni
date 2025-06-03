from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    #path('login/', views.CustomLoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
]