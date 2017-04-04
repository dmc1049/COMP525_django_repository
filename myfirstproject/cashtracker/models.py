#https://docs.djangoproject.com/en/1.10/topics/db/models/
#https://docs.djangoproject.com/en/1.10/ref/models/fields/

from django.db import models
from django.utils import timezone

# Create your models here.

class Receipt(models.Model):
	merchandise = models.CharField(max_length = 30)
	purchase_date = models.DateTimeField(default = timezone.now)
	price = models.CharField(max_length = 16)
	
	def __str__(self):
		return self.merchandise + ',' + self.price
		
