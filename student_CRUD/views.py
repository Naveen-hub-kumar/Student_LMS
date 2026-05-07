from django.shortcuts import render 
from .models import studentDetails



# Create your views here.
def homepage(request) :
        students_list = studentDetails.objects.all()
        context  = {
                "students" : students_list
        }
        return render(request, "homepage.html" , context)

def add_student(request) :
        return render(request, "add_student.html")