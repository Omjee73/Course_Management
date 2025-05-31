from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course, Student
from .forms import StudentForm

class CustomUserAdmin(UserAdmin):
    # Sirf yeh fields dikhana chahte hain
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active',)}),  # sirf is_active dikhaye
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active'),
        }),
    )

# Purane UserAdmin ko unregister kar ke custom wala register karo
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class StudentInline(admin.TabularInline):
    model = Student
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields] + ['student_count']
    search_fields = [field.name for field in Course._meta.fields if field.get_internal_type() in ['CharField', 'TextField']]
    list_filter = [field.name for field in Course._meta.fields if field.get_internal_type() in ['CharField', 'BooleanField', 'DateField', 'ForeignKey']]
    actions = ['combine_courses']
    inlines = [StudentInline]

    def student_count(self, obj):
        return obj.students.count()
    student_count.short_description = 'Student Count'

    @admin.action(description='Combine selected courses')
    def combine_courses(self, request, queryset):
        if queryset.count() < 2:
            self.message_user(request, "Please select at least two courses to combine.", level=messages.ERROR)
            return

        # Combine names and descriptions
        combined_name = " + ".join([course.name for course in queryset])
        combined_description = "\n\n".join([course.description for course in queryset])

        # Create new course
        new_course = Course.objects.create(name=combined_name, description=combined_description)

        # Move all students to new course
        Student.objects.filter(course__in=queryset).update(course=new_course)

        self.message_user(request, f"Combined course '{combined_name}' created with all students from selected courses.")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['user', 'get_first_name', 'get_last_name', 'get_email', 'get_username', 'course']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email']
    list_filter = ['course']
    actions = ['deactivate_users_and_delete']

    def get_first_name(self, obj):
        return obj.user.first_name if obj.user else ''
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name if obj.user else ''
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email if obj.user else ''
    get_email.short_description = 'Email'

    def get_username(self, obj):
        return obj.user.username if obj.user else ''
    get_username.short_description = 'Username'

    @admin.action(description="Deactivate user and delete student")
    def deactivate_users_and_delete(self, request, queryset):
        for student in queryset:
            if student.user:
                student.user.is_active = False
                student.user.save()
            student.delete()
