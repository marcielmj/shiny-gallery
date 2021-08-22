from django.urls import path

from .views import UserCreateView, UserLoginView, UserLogoutView


app_name = "users"

urlpatterns = (
    path("signup/", UserCreateView.as_view(), name="user-signup"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("logout/", UserLogoutView.as_view(), name="user-logout"),
)
