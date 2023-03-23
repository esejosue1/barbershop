from django.db import models

# Create your models here.
class Barbers(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/barbers')
    title=models.CharField(max_length=100, null=True)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    instragram=models.CharField(max_length=500, blank=True)
    facebook=models.CharField(max_length=500, blank=True)
    twitter=models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name='Barber'
        verbose_name_plural='Barbers'

    def __str__(self):
        return self.first_name
  