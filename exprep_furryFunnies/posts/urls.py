from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('<int:id>/', include([
        path('details/', views.PostDetailsView.as_view(), name='details-post'),
        path('edit/', views.PostEditView.as_view(), name='edit-post'),
    ])),
]
