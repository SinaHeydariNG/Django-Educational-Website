from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(max_length=225)
    description = RichTextField()
    location = models.CharField(max_length=225 , default=1)
    phone = models.CharField(max_length=225 , default=1)
    logo = models.ImageField(upload_to = 'logo/%y/%m/%d/')
    email = models.EmailField(default='imsinacoder@gamil.com')
    copyright = models.CharField(max_length=225)

    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Informations" 

    def __str__(self):
        return "YOUR SITE INFO . DONT ADD ANOTHER ONE !!!"

class Socials(models.Model):
    title = models.CharField(max_length=225)
    url = models.URLField()
    img = models.ImageField(upload_to = 'socials/%y/%m/%d')
    