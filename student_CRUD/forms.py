from django import forms
from .models import studentDetails

class studentForm(forms.ModelForm):
    class Meta:
        model=studentDetails
        fields=["student_name","email","course","enrollment_date"]