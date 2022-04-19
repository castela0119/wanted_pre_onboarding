from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

from apps.products.models import Products

class User(AbstractUser):
   email = models.EmailField(verbose_name='email', unique=True)
   username = models.CharField(verbose_name='username', max_length=25)
   password = models.CharField(max_length=25)

   products = models.ManyToManyField(Products, default={})

   created_at = models.DateField(default=timezone.now)

   USERNAME_FIELD = 'email'  # email 로 로그인

   # 필수로 받고 싶은 필드들 넣기 원래 소스 코드엔 email필드가 들어가지만 우리는 로그인을 이메일로
   REQUIRED_FIELDS = ['username', 'password']

   class Meta:
        verbose_name_plural = "유저목록"
        db_table = "users"

   def __str__(self):
       return self.username



# class UserManager(BaseUserManager):
#     def create_user(self, user_ID, email, password):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError("Users must have an email address")

#         user = self.model(
#             user_ID=user_ID,
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_ID, email, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             user_ID=user_ID,
#             email=email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     user_ID = models.CharField(verbose_name="유저아이디", max_length=150, unique=True)
#     email = models.EmailField(
#         verbose_name="이메일",
#         max_length=255,
#         unique=True,
#     )
#     created_at = models.DateField(default=timezone.now)

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = "user_ID"
#     REQUIRED_FIELDS = ["email"]

#     class Meta:
#         verbose_name_plural = "사용자"
#         db_table = "user"

#     def __str__(self):
#         return self.user_ID

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin
