from django.contrib.gis import admin
from apps.green import models
# Register your models here.


admin.site.register(models.Stand, admin.OSMGeoAdmin)
admin.site.register(models.Center)
admin.site.register(models.Produce)
# we want to see this model in the admin page, above code does this
