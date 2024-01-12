from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName= models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 20, null=True)
    
    def __str__(self):
        return self.firstName + " " + self.lastName

class Department(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Office(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
