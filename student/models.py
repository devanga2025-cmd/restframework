from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    student_class=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.name
