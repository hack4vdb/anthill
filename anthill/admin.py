from django.contrib import admin
from anthill import models

# Register your models here.

admin.site.register(models.Activist)
admin.site.register(models.Meetup)
admin.site.register(models.Participation)
admin.site.register(models.PostalcodeCoordinates)
