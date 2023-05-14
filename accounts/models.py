from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)  
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
