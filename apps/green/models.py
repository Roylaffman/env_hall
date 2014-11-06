from django.contrib.gis.db import models

# Create your models here.


class Center(models.Model):
    """This model holds recycling centers"""
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.PointField(srid=4326)
    glass = models.BooleanField(default=False)
    paper = models.BooleanField(default=False)
    aluminum = models.BooleanField(default=False)
    plastic = models.BooleanField(default=False)
    oil = models.BooleanField(default=False)
    rechargeBatteries = models.BooleanField(default=False)
    electronics = models.BooleanField(default=False)
    paint = models.BooleanField(default=False)
    tires = models.BooleanField(default=False)
    cookGrease = models.BooleanField(default=False)
    scrapMetal = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)


