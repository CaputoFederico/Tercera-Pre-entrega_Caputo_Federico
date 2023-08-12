from django.db import models

# Create your models here.
class star_trek(models.Model):
    serie=models.CharField(max_length=256)
    temporadas= models.IntegerField()
    pilot= models.IntegerField()

    def __str__(self):
        return f"{self.serie}, {self.temporadas}, {self.pilot}"


class star_wars(models.Model):
    serie=models.CharField(max_length=60)
    temporadas= models.IntegerField()
    pilot= models.IntegerField()

    def __str__(self):
         return f"{self.serie}, {self.temporadas}, {self.pilot}"


class otras_series(models.Model):
    serie=models.CharField(max_length=60)
    temporadas= models.IntegerField()
    pilot= models.IntegerField()
    saga=models.CharField(max_length=80)

    def __str__(self):
         return f"{self.saga},{self.serie}, {self.temporadas}, {self.pilot}"

# Create your models here.
