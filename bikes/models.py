from django.db import models

# Create your models here.

class Bike(models.Model):
	idn = models.CharField(default="None",max_length=5)
	poi_x = models.CharField(default="0.0",max_length=5)
	poi_y = models.CharField(default="0.0", max_length=5)

	last_modify_date = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		db_table = "bikes"

	def __str__(self):
		return self.idn
