from django.db import models

# Create your models here.
class Fruit(models.Model):
    full_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    scientific_name=models.CharField(max_length=100)
    use=models.CharField(max_length=100)
    season=models.CharField(max_length=100)
    cost=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.full_name