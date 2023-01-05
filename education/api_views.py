from django.http import JsonResponse
from rest_framework import generics
from education.models import *
from education.serializers import *
from rest_framework import authentication, permissions


# .../semester/ -> GET:list, POST:create
class SemesterListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]  # AdminUser: staff


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

