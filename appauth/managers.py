from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class StaffManager(BaseUserManager):

    """
    Custom user model manager where staff_number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, staff_number, password, **extra_fields):
        """
        Create and save a User with the given staff_number and password.
        """
        if not staff_number:
            raise ValueError(_('The Staff Number must be set'))
        staff_number = staff_number
        user = self.model(staff_number=staff_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staff_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given staff_number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(staff_number, password, **extra_fields)