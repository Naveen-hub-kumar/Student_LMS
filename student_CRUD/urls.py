from django.contrib import admin
from django.urls import path 
from student_CRUD import views



urlpatterns = [
    path("", views.homepage, name="homepage"), 
    path("add_student/", views.add_student, name="add_student"), 

]