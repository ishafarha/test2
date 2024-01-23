from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class persons(models.Model):
    names = models.CharField(max_length=250)
    imgs = models.ImageField(upload_to='pics')
    descp = models.TextField()

    def __str__(self):
        return self.names
