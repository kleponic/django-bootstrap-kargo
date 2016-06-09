from __future__ import unicode_literals

import uuid as uuid

from django.db import models

class CommonInfo(models.Model):
    """
    Abstract models contains mandatory fields on each models.
    Every class can have these fields by instantiate from this class.
    """
    remarks = models.TextField(blank=True, verbose_name='Keterangan Tambahan')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Waktu Dibuat')
    modified = models.DateTimeField(auto_now=True, verbose_name='Waktu diedit')
    status = models.BooleanField(default=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    # flag for update, delete, sync and coming from cloud
    is_delete = models.BooleanField(default=False, verbose_name='Soft Delete')

    class Meta:
        abstract = True


class ODVehicle(CommonInfo):
    """
    Vehicle models contains  name, driver, number, and capacity
    """
    name = models.CharField(max_length=50)
    driver = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    photo = models.ImageField(upload_to = 'upload/', default = 'upload/no-img.png')

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __unicode__(self):
        return self.name

    
    
