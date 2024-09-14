from django.db import models

# Create your models here.

class Links(models.Model):

    def __str__(self):
        return self.address
    
    name=models.CharField(max_length=1000,null=True,blank=True)
    address=models.CharField(max_length=1000,null=True,blank=True)