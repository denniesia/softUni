from django.template.context_processors import request
from drf_spectacular.utils import extend_schema
from todo_djangorest.accounts.serializers import UserSerializer, LoginRequestSerializer, LoginResponseSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

UserModel = get_user_model()
class RegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(
    tags=['auth'],
    summary="Login endpoint",
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        401: 'Invalid credentials',
    }
)
class LoginView(APIView):
   permission_classes = [AllowAny]

   def post(self, request, *args, **kwargs):
       username = request.data.get('username')
       password = request.data.get('password')

       user = authenticate(username=username, password=password)

       if user is None:
           return Response(
               {
                   "error": 'Invalid credentials'
               },
               status=status.HTTP_401_UNAUTHORIZED,
           )

       refresh = RefreshToken.for_user(user) #returns an object
       from rest_framework import status
       return Response({
           "refresh": str(refresh),
           "access": str(refresh.access_token),
           "message": "Successfully logged in.",
       }, status=status.HTTP_200_OK
       )