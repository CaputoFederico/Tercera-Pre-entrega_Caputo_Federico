from django.db import models

# Create your models here.
class Star_Trek(models.Model):

    serie=models.CharField(max_length=40)
    temporadas= models.IntegerField()
    pilot= models.IntegerField()

    def __str__(self):
        return f"{self.serie}, N° de temporadas: {self.temporadas}, {self.pilot}"


class Star_Wars(models.Model):

    serie=models.CharField(max_length=40)
    temporadas= models.IntegerField()

    def __str__(self):
        return f"{self.serie}, N° de temporadas: {self.temporadas}"


class Otras_Series(models.Model):

    serie=models.CharField(max_length=40)
    temporadas= models.IntegerField()

    def __str__(self):
        return f"{self.sergie}, N° de temporadas: {self.temporadas}"