from rest_framework.serializers import ModelSerializer

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
    class Meta:
        model = Student
        exclude = ['password']


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Student
        exclude = ['password']
