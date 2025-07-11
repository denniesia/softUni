from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, authenticate, login, get_user_model
from django.views import generic as views
from django.contrib.auth import forms as auth_forms
from .forms import CreateUserForm
# Create your views here.

# UserModel = get_user_model()

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'

    # def get_success_url(self):
    #     return reverse_lazy('index')


class RegisterUserView(views.CreateView):
    # form_class = auth_forms.UserCreationForm
    form_class = CreateUserForm
    template_name = 'accounts/register_user.html'
    success_url = reverse_lazy('index')

# class CustomLoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class(),
#         }
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         username, password = request.POST['username'], request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         print(user)
#
#         if user is not None:
#             login(request, user)
#
#         return redirect('index')

