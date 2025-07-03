from rest_framework_simplejwt.views import TokenRefreshView
from todo_djangorest.accounts.views import RegisterView, LoginView, LogoutApiView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]