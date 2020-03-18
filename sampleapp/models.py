from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class UserProfile(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email",max_length=60, unique=True,default='')
	username 				= models.CharField(max_length=30,default='Null')
	password 				= models.CharField(verbose_name='password',max_length=16)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)



	objects = MyAccountManager()

	USERNAME_FIELD = 'username'
	EmailField = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email
