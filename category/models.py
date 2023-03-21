from django.db import models

# Create your models here.


#create services model
class typeOfService(models.Model):
    type_of_service=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    

    class Meta:
        verbose_name='Types of Service'
        verbose_name_plural='Types of Service'

    def __str__(self):
        return self.type_of_service
    
class Services(models.Model):
    type_of_service=models.ForeignKey(typeOfService, on_delete=models.CASCADE)
    service=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    price=models.IntegerField()
    description=models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

    def __str__(self):
        return self.service