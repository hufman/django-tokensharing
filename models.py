from django.db import models

class AuthToken(models.Model):
	token = models.CharField(max_length=40)
	directory = models.TextField(max_length=700)
	expiration = models.DateTimeField('expiration')
	note = models.CharField(max_length=40)
