from django.contrib import admin
from django.urls import path 
from student_CRUD import views



urlpatterns = [
    path("", views.homepage, name="homepage"), 
    path("add_student/", views.add_student, name="add_student"), 
    path( "details/<int:id>/",views.details,name="details"),
    path( "delete/<int:id>/",views.delete_student,name="delete_student"),
    path("api/student/",views.StudentListCreationAPI.as_view(),name="Student-List-Creation-API")


]