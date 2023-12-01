from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20)
    material1 = models.BooleanField(default=False)
    material2 = models.BooleanField(default=False)

    def __str__(self):
        return self.name

