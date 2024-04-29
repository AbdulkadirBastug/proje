from django.db import models

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    FinalGrade=models.DecimalField(max_digits=5,decimal_places=2)
    CreatedAt=models.DateTimeField(auto_now=True)