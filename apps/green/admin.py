from django.contrib.gis import admin
from apps.green import models
# Register your models here.  It allows them to be seen in the admin page.


admin.site.register(models.Stand, admin.OSMGeoAdmin)
admin.site.register(models.Center)
admin.site.register(models.Produce)

