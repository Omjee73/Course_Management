from django.contrib import admin
from .models import Student, Course
from .forms import StudentForm

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['user', 'get_courses', 'age', 'contact']

    def get_courses(self, obj):
        return ", ".join([c.name for c in obj.enrolled_courses.all()])
    get_courses.short_description = "Courses"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    actions = ['combine_courses']

@admin.action(description='Combine selected courses')
def combine_courses(self, request, queryset):
    if queryset.count() < 2:
        self.message_user(request, "Please select at least two courses to combine.", level=messages.ERROR)
        return

    combined_name = " + ".join([course.name for course in queryset])
    combined_description = "\n\n".join([course.description for course in queryset])
    new_course = Course.objects.create(name=combined_name, description=combined_description)

    # Get all unique students from selected courses
    students = Student.objects.filter(enrolled_courses__in=queryset).distinct()
    for student in students:
        student.enrolled_courses.add(new_course)

    self.message_user(
        request,
        f"Combined course '{combined_name}' created. {students.count()} unique students enrolled."
    )
