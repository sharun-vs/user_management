from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
	def create_user(self, username, full_name, email, password=None):
		if not email:
			raise ValueError("users must have an email address!")

		user = self.model(
			username = username,
			full_name = full_name,
			email = self.normalize_email(email)),

		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, username, full_name, email, password=None):
		user = self.create_user(
			username,
			full_name,
			email,
			password=password
			)
		user.is_admin = True
		user.save(using = self._db)
		return user

class User(AbstractBaseUser):
	username = models.CharField(max_length=50, unique=True)
	full_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=255, unique=True)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'

	def __str__(self):
		return self.email