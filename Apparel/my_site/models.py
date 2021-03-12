from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    object =models.manager

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.IntegerField()
    photo = models.ImageField(upload_to='uploadImage/')
    catName = models.ForeignKey(category, on_delete=models.CASCADE)

    object = models.manager

    def __str__(self):
        return self.name

