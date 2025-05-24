from django.urls import path, include
from . import  views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('authors/', include('authors.urls')),
    path('posts/', include('posts.urls')),
]
