from django.db import models

# Create your models here.
class studentDetails(models.Model):
    student_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique=True)
    course=models.CharField(max_length=75)
    enrollment_date=models.DateField()

    def __str__(self):
        return self.student_name