from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=10)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

