from django.db import models

class Item(models.Model):
    label = models.CharField(max_length=255, blank=False, null=False)
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="static/images/items", max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label
