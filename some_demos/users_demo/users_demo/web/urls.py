from django.urls import path
from users_demo.web.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]