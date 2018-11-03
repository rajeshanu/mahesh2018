from django.db import models

# Create your models here.
class product(models.Model):
    idno=models.IntegerField(default=4,primary_key=True)
    name=models.CharField(max_length=75)
    salary=models.DecimalField(max_digits=6,decimal_places=2)