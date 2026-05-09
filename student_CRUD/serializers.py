from rest_framework import serializers
from .models import studentDetails



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=studentDetails
        fields=['student_name','email','course','enrollment_date']
