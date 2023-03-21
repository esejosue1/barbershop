from django.db import models

# Create your models here.


#create services model
class typeOfService(models.Model):
    type_of_service=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.type_of_service
    
