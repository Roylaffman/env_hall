# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=200)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('glass', models.BooleanField(default=False)),
                ('paper', models.BooleanField(default=False)),
                ('plastic', models.BooleanField(default=False)),
                ('oil', models.BooleanField(default=False)),
                ('rechargeBatteries', models.BooleanField(default=False)),
                ('electronics', models.BooleanField(default=False)),
                ('cellPhones', models.BooleanField(default=False)),
                ('paint', models.BooleanField(default=False)),
                ('tires', models.BooleanField(default=False)),
                ('cookGrease', models.BooleanField(default=False)),
                ('scrapMetal', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
