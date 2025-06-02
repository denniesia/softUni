from django.urls import path
from users_demo.web.views import index

urlpatterns = [
    path('', index, name='index'),
]