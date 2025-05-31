from rest_framework import serializers
from .models import Course, Student
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    enrolled_courses = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        many=True,
        required=False,  # blank option
        allow_null=True
    )

    class Meta:
        model = Student
        fields = ['user', 'enrolled_courses', 'age', 'contact']

    def validate_enrolled_courses(self, value):
        if len(value) > 4:
            raise serializers.ValidationError("You can select up to 4 courses only.")
        return value
