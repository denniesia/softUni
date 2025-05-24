from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('<int:id>/details/', views.PostDetailsView.as_view(), name='details-post'),

]
