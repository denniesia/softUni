from django.urls import  path
from . import views


urlpatterns = [
    path('', views.ListBooksView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
]