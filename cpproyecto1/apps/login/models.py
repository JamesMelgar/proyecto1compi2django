from django.db import models

#si quiero crear un modelo

class mlogin(models.Model):
	nombre = models.CharField(max_length = 50)
	contraseña =  models.CharField(max_length = 50)
# Create your models here.
