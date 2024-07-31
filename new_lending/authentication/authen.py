from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend, ModelBackend


class AuthenticationEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email = username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return 'Error. This user already exist'

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None


