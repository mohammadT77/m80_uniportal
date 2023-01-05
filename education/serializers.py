from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from education.models import *


class SemesterSerializer(ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DegreeSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True) # serializers.StringRelatedField(many=True, read_only=True)
    # degree = serializers.StringRelatedField(queryset=Degree.objects.all(), many=False, read_only=True)

    class Meta:
        model = Student
        exclude = ['password', 'is_staff', 'is_superuser']



class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Student
        exclude = ['password']


class StudentCourseSerializer(ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
