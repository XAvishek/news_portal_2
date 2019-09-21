from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    ROLES = (('0','Admin'),('1','Reporter'),('2','Guest'))
    role = models.CharField(choices=ROLES, default='2', max_length= 1)
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ('first_name','last_name', 'email')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=50)
