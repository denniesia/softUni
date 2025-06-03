from django.urls import path
from . import views
urlpatterns = [
    #path('login/', views.LoginUserView.as_view(), name='login'),
    path('login/', views.CustomLoginUserView.as_view(), name='login'),
]