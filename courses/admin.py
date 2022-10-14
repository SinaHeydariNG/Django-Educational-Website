from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Courses)
admin.site.register(models.Category)
admin.site.register(models.Episodes)