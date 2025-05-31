from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    enrolled_courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # or forms.SelectMultiple for dropdown
        required=True
    )

    class Meta:
        model = Student
        fields = ['user', 'enrolled_courses', 'age', 'contact']