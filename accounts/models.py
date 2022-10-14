
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from ckeditor.fields import RichTextField
from courses.models import Courses
from datetime import datetime

class CustomUser(AbstractUser):
    username = models.CharField(max_length=225 , unique=True)
    email = models.EmailField(('email address'), unique=True , )
    image = models.ImageField((' profile picture '),upload_to='profile/' , blank = True)
    first_name = models.CharField(max_length=225 , blank=True)
    last_name = models.CharField(max_length=225 , blank=True)
    birthday = models.DateField(blank=True , null=True)
    address = models.CharField(max_length=225 , blank=True)
    phone_number = models.CharField(max_length=225 , blank=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class MessageSubjecs(models.TextChoices):
    PROJECT = "PROJECT" , "PROJECT"
    WORK = "WORK" , "WORK"
    OTHER = "OTHER" , "OTHER"

class Messages(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    title = models.CharField(max_length=225 , )
    subject = models.CharField(max_length=10 , choices=MessageSubjecs.choices , default=MessageSubjecs.PROJECT)
    text = RichTextField()
    response = models.TextField(null=True , blank = True)
    activate = models.BooleanField(blank=True , null=True , default=False)

    def __str__(self):
        return "{} from {}".format(self.title , self.user)

class SavedCourses(models.Model):
    courses = models.ManyToManyField(Courses)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , related_name='saved')
    activate = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return "{}'s Saved Courses".format(self.user)