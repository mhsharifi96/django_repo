from django.db import models

# Create your models here.


class testModel(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
    upload = models.FileField(upload_to='uploads/',null=True)