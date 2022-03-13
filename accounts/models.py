from datetime import datetime
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        # error handling
        if not email:
            raise ValueError('User must have email address')
        
        if not username:
            raise ValueError('User must have username')
        
        user = self.model(
            # normalizing meaning if any user enter email address in capital or small-capital mix, it'll automatically set to small alphabet
            email=self.normalize_email(email), 
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        
        # extra required fields for superusers
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # required
    # automatically added account joining date
    date_joined = models.DateTimeField(auto_now_add= True)
    # automatically added last account login date
    last_login = models.DateTimeField(auto_now_add= True)
    # checkbox type field
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    # this field will be used for admin login
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    
    objects = MyAccountManager()
    
    def __str__(self) -> str:
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True