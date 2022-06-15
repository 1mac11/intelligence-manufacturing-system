from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from core.managers import UserManager
from core.models.user_role import UserRoleChoice


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    role = models.ForeignKey('core.UserRole', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    personal = models.JSONField(default=dict)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    objects = UserManager()

    user_permissions = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email

    def is_owner(self):
        return self.role.name == UserRoleChoice.OWNER
