import shapefile
from apps.green.models import Center
import django
django.setup()

center_path = 'C:/Users/crswin5726/PycharmProjects/env_hall/apps/green/data/centers.shp'
#person_path = 'C:/Users/Crystal/Desktop/ShapefileEdits/Person_Master.shp'

sf = shapefile.Reader(center_path)
sr = sf.shapeRecords()
record = {-1: True, 0: False}

for r in sr:

    m = Center(name=r.record[0], address=r.record[1], lon=r.record[2], lat=r.record[3],
               glass=record[r.record[4]], paper=record[r.record[5]],
               aluminum=record[r.record[6]], plastic=record[r.record[7]],
               oil=record[r.record[8]],  rechargeBatteries=record[r.record[9]],
               electronics=record[r.record[10]], paint=record[r.record[11]],
               tires=record[r.record[12]], cookGrease=record[r.record[13]],
               scrapMetal=record[r.record[14]],
               geom="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    print(r.record[0], r.record[1], r.record[2], r.record[3], r.record[4],
          r.record[5], r.record[6], r.record[7], r.record[8], r.record[9],
          r.record[10], r.record[11], r.record[12], r.record[13], r.record[14], r.shape.points)
    m.save()

