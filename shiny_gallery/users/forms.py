from django.contrib.auth import forms

from .models import User


class UserCreateForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")
        field_classes = {"username": forms.UsernameField}
