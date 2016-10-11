from .models import AppUser


class AppAuthBackend:
    def authenticate(self, username=None, password=None):
        try:
            user = AppUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except AppUser.DoesNotExist:
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return None
