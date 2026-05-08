from django.shortcuts import render,redirect,get_object_or_404
from .models import studentDetails
from .forms import studentForm
from django.http import HttpResponse



# Create your views here.
def homepage(request) :
        students_list = studentDetails.objects.all()
        context  = {
                "students" : students_list
        }
        return render(request, "homepage.html" , context)

def add_student(request) :
        if request.method == "POST" :
                form = studentForm(request.POST)
                if form.is_valid() :
                        form.save()
                        return redirect("homepage")
        
        form = studentForm()
        context = {
                "form" : form
        }
        return render(request, "add_student.html", context)


def details(request, id) :
        if request.method == "POST" :
                student = get_object_or_404(studentDetails, pk=id)
                form = studentForm(request.POST, instance=student)
                if form.is_valid() :
                        form.save()
                        return redirect("homepage")
        
        student = get_object_or_404(studentDetails,pk=id)
        form = studentForm(instance=student)
        context = {
              "form" : form
      }
        return render(request, "view_detail.html", context)

def delete_student(request, id) :
        student = get_object_or_404(studentDetails, pk=id)
        student.delete()
        return redirect("homepage")