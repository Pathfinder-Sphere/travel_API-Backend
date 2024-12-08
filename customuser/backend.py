from .models import CustomUser
from django.contrib.auth.backends import BaseBackend

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return CustomUser.objects.get(pk=email)
        except CustomUser.DoesNotExist:
            return None  
