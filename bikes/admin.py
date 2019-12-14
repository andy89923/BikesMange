from django.contrib import admin


# Register your models here.
from bikes.models import Bike


class BikeAdmin(admin.ModelAdmin):
	list_display = ('idn', 'poi_x', 'poi_y')
	search_fields = ('idn', )
	ordering = ('idn', )

admin.site.register(Bike, BikeAdmin)


