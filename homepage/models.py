from django.db import models

class Item(models.Model):
    label = models.CharField(max_length=255, blank=False, null=False)
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="static/images/items", max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.label

class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    short_description = models.CharField(max_length=255, blank=False, null=False)
    long_description = models.TextField(blank=False, null=False)
    project_url = models.CharField(max_length=255, blank=False, null=False)
    github_url = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to="static/images/projects", max_length=255, blank=True, null=True)
    display_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
