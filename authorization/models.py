from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


# class AppUserManager(UserManager):
#     def create_user(self, username, email=None, password=None, age=None, **extra_fields):
#         user = self.model(email='email', age=0, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password, **extra_fields):
#         user = self.create_user(username=username, email=email, password=password)
#         user.save(using=self._db)
#         return user
#
#
# class AppUser(AbstractUser):
#     age = models.IntegerField(default=0)
#     objects = AppUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = _('user')


class AppUserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class AppUser(AbstractUser):
    receive_newsletter = models.BooleanField('receive newsletter', default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # def get_full_name(self):
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()
    #
    # def get_short_name(self):
    #     return self.first_name
    #
    # def email_user(self, subject, message, from_email=None):
    #     send_mail(subject, message, from_email, [self.email])
