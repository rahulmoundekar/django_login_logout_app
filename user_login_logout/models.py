from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=45, unique=True, )
    password = models.CharField(max_length=45)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that is built in.
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.is_superuser

    @property
    def is_active(self):
        "Is the user active?"
        return self.is_active

    class Meta:
        db_table = "user"


class LoginUser(models.Model):
    name = models.CharField(max_length=45)
    mobile = models.CharField(max_length=10)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, primary_key=True, )

    class Meta:
        db_table = "login_user"
