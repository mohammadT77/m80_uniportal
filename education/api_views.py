from django.http import JsonResponse
from rest_framework import generics
from education.models import *
from education.serializers import *
from rest_framework import authentication, permissions, pagination


# .../semester/ -> GET:list, POST:create
class SemesterListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()
    throttle_scope = 'education'

    permission_classes = [permissions.IsAuthenticated,
                          permissions.DjangoModelPermissions]  # AdminUser: staff



# .../semester/5 -> GET: details, PUT/PATCH: modify, DELETE: destroy
class SemesterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()

    lookup_field = 'id'  # Semester.id
    lookup_url_kwarg = 'pk__'


# .../course/ -> GET:list, POST:create
class CourseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# .../course/5 -> GET: details, PUT/PATCH: modify, DELETE: destroy
class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    lookup_field = 'id'  # Course.id
    lookup_url_kwarg = 'pk__'


# .../Student/ -> GET:list, POST:create
class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


# .../Student/5 -> GET: details, PUT/PATCH: modify, DELETE: destroy
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    lookup_field = 'username'  # Student.id
    lookup_url_kwarg = 'username'


class StudentCourseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentCourseSerializer
    queryset = StudentCourse.objects.all()

    # student/{sid}/course/ -> List enrolled courses by the student
    def get_queryset(self):
        if 'student' in self.kwargs:  # .../<int:sid>/...
            return StudentCourse.objects.filter(student__username=self.kwargs['student'])
        return super().get_queryset()  # .../.../...

