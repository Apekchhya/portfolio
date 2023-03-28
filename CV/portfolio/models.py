from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=200, blank=True, default=None)
    description = models.TextField(blank=True, default=None)
    key_interest = models.CharField(max_length=200)
    profile_image = models.ImageField()

class Experience(models.Model):
    image = models.ImageField()
    company = models.CharField(max_length=200, blank=True, default=None)
    description = models.TextField(blank=True, default=None)
    date = models.DateTimeField(auto_now=True)
    location = models.TextField(null=True, blank=True, default=None)

class Project(models.Model):
    title = models.TextField(null = True, blank = True,  default=None)
    description = models.TextField(null=True, blank = True,  default=None)
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    title =models.CharField(max_length=200, null=True, blank=True, default=None)
    image = models.ImageField()

class Header(models.Model):
    name = models.CharField(max_length=200)
    affiliation = models.TextField(blank=True, default = None)
    location = models.CharField(max_length=200, blank=True, default=None)

class Footer(models.Model):
    title = models.TextField(blank=True, default=None)
    location = models.TextField(blank=True, default = None)
    phone = models.TextField(blank=True, default=None, null=True)
    gmail = models.EmailField(blank=True, default=None)
    linkedin = models.URLField(blank=True, default = None)
    github = models.URLField(blank=True, default = None)

class Publication(models.Model):
    title = models.TextField()
    journal = models.TextField()
    url = models.URLField(null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now=True)

class Certification(models.Model):
    title = models.TextField()
    org = models.TextField(null=True, blank=True, default=None)
    image = models.ImageField(null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now=True)

class Education(models.Model):
    school = models.TextField()
    year = models.TextField()
    gpa = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    degree = models.TextField()
    location = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Award(models.Model):
    title = models.TextField()
    org = models.TextField()
    image = models.ImageField(null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title

class Meta:
    abstract = True
    ordering = ['-date']