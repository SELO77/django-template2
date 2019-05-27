from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    # name = CharField(_("Name of User"), blank=True, max_length=255)
    username = models.CharField(
        _('username'),
        max_length=150,
        null=True
    )
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.email})
