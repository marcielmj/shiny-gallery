from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreateForm
from .models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy("users:user-login")


class UserLoginView(LoginView):
    template_name = "users/user_login.html"


class UserLogoutView(LogoutView):
    template_name = "users/user_logout.html"
