from django import forms
from django.contrib.auth.models import User
from .models import Student, Course

class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'username', 'course']

    def save(self, commit=True):
        data = self.cleaned_data
        username = data['username']
        # Try to get existing user by username
        user = None
        if self.instance.pk and self.instance.user:
            user = self.instance.user
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.is_active = True
        user.save()
        student = super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'