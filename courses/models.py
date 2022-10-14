from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from datetime import datetime
# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length = 225)
    price = models.DecimalField(decimal_places = 2 , max_digits=7)
    discount = models.IntegerField(blank = True , null = True)
    thumbnail = models.ImageField(upload_to='courses/%y/%m/%d')
    information = models.TextField()
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    slug = models.SlugField(null=True , blank = True)

    def cut_info(self):
        return "{} ...".format(self.information[:30])

    def discounted(self):
        return (self.price * self.discount) / 100

def slugify_pre_save(sender , instance , *args , **kwargs):
    title = instance.title
    slug = instance.slug
    if slug is None:
        instance.slug = slugify(title)

class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class Locked(models.TextChoices):
    AVAILABEL = "AVAILABEL" , "AVAILABEL",
    LOCKED = "LOCKED" , "LOCKED",

class Episodes(models.Model):
    title = models.CharField(max_length = 225)
    thumbnail = models.ImageField(upload_to='episodes/%y/%m/%d')
    information = models.TextField()
    status = models.CharField(max_length=10 , choices=Locked.choices , default=Locked.AVAILABEL)
    course = models.ForeignKey(Courses , on_delete=models.CASCADE , related_name='episodes')



    def __str__(self):
        return  "{} from {} at {}".format(self.course , self.user , self.added) 



pre_save.connect(slugify_pre_save , Courses)