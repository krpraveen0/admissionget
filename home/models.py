from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class EnggCollege(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.title 

class MedicalCollege(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class MmgCollege(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class LawCollege(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.title

#model for courses
class Courses(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=150)
    intro = RichTextField(blank=True, null=True)
    degree = RichTextField(blank=True, null=True)
    career = RichTextField(blank=True, null=True)
    topCol = RichTextField(blank=True, null=True)
    admsnProcess = RichTextField(blank=True, null=True)
    admsnGuid = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=180)

    def __str__(self):
        return 'Content from ' + self.title 


#contact form model
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + "-" + self.email
