from django.contrib import admin
from .models import studentDetails

# Register your models here.
#admin.site.register(studentDetails)

class StudentAdmin(admin.ModelAdmin):
    list_display=("student_name","email","course","enrollment_date")
    search_fields=("studen_name","email","course")
    list_filter=("course",)

admin.site.register(studentDetails,StudentAdmin)