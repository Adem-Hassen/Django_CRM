from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)
    def __str__(self) :
        return (f"{self.First_name} {self.Last_name}")
    