from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)

    gender_choices=[

        ('male','Male'),('female','Female')             #first database,second client view
    ]
    gender=models.CharField(max_length=20,choices=gender_choices)

    joining_date=models.DateField()
    # joining_date = models.DateField(auto_now_add=True)     #it will add date and time automatically

    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    image = models.ImageField(upload_to="movies", null=True)