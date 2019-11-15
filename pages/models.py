from django.db import models
from PIL import Image
# Create your models here.


class Philosophy(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'static_images')
    title = models.CharField(max_length = 100, default = '')
    content = models.TextField(max_length = 500, null=True)

    class meta:
        verbose_name_plural = "Philosophies"

    def __str__(self):
        return self.title

class Mission(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 500, null=True)

    def __str__(self):
        return self.title

class Vision(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 500, null=True)

    def __str__(self):
        return self.title

class Virtues(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 500, null=True)

    def __str__(self):
        return self.title

class Prayer(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 1000, null=True)

    def __str__(self):
        return self.title

class PhysicalAddress(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 1000, null=True)

    def __str__(self):
        return self.title

class MailingAddress(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 1000, null=True)

    def __str__(self):
        return self.title


class ContactPerson(models.Model):
    name = models.CharField(max_length = 200, default = '')
    position = models.CharField(max_length = 200, default = '')
    social_media = models.CharField(max_length = 200, default = '')


    def __str__(self):
        return self.name


class ExtraContact(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 1000, null=True)

    def __str__(self):
        return self.title

class DrivingDirection(models.Model):
    title = models.CharField(max_length = 100, default = '')
    content = content = models.TextField(max_length = 1000, null=True)

    def __str__(self):
        return self.title
