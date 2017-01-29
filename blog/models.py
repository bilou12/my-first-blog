from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')], blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=50)
    state = models.CharField(blank=True, max_length=50)
    zip_code = models.CharField(blank=True, max_length=12)
    verified = models.NullBooleanField(blank=True, null=True)
    ambassador_super_user = models.NullBooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now, null=True)
    last_connection_date = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Hobby(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)


class Comment(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=500)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)s_teacher_related")
    student = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)s_student_related")
