from todo_djangorest.accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.

UserModel = get_user_model()
class RegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]