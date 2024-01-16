from django.db import models

# Create your models here.

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

class Employee(models.Model):
    firstName= models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 20, null=True)
    department = models.ForeignKey(Department ,on_delete=models.CASCADE,null=True)
    office = models.ForeignKey(Office, on_delete= models.CASCADE,null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE,null=True)
    profile_pic = models.ImageField(null=True , blank=True)
    
    def __str__(self):
        return self.firstName + " " + self.lastName
