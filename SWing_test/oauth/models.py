from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from datetime import datetime
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, student_id, email, username, password=None): #create_superuser과는 permission 차이
        #try:
        user = self.model(
            student_id=student_id,
            email=email,
            username=username
        )
        user.set_password(password)
        user.is_active=True
        user.save()
        return user
        #except Exception as e:
        #    print(e)
    
    def create_superuser(self, student_id, email, username, password=None):
        try:
            superuser = self.create_user(
                student_id=student_id,
                email=email,
                username=username,
                password=password
            )
            superuser.is_admin=True
            superuser.is_superuser=True
            superuser.is_staff=True
            superuser.save()
            return superuser
        except Exception as e:
            print(e)
            
    

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()
    
    student_id = models.CharField(
        unique=True,
        max_length=8,
    )
    
    email = models.EmailField(
        max_length=30,
        unique=True,
    )
    
    
    username = models.CharField(max_length=20, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    first_name = models.CharField(max_length=20, default = ' ')
    last_name = models.CharField(max_length=20, default = ' ')
    date_joined = models.DateTimeField(default=datetime.now)####수정필요(time field 못받아옴)
    
    USERNAME_FIELD = 'student_id' #로그인할때 id (학번)
    REQUIRED_FIELDS = ['email', 'username'] #유저 생성시 필수요소
    
    def __str__(self):
        return str(self.student_id)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return self.is_admin