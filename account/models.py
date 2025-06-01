from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin

roles = (
    ("admin", "Admin"),
    ("operator", "Operator"),
    ("doctor", "Doctor"),
    ("compounder", "Compounder")
)

class UserManager(BaseUserManager):
    def create_user(self,username,password=None, **extra_fields):
        if not username:
            raise ValueError("User must have an username")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("role", "admin")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have an is_staff True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have an is_superuser True")
        user = self.create_user(username,password,**extra_fields)
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(max_length=80)
    role = models.CharField(choices=roles, max_length=70)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'
    
    objects = UserManager()
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    