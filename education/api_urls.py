from django.urls import path
from .api_views import *

urlpatterns = [
    path('semester/', SemesterListCreateAPIView.as_view(), name='semester_lc_view'),
    path('semester/<int:pk__>', SemesterRetrieveUpdateDestroyAPIView.as_view(), name='semester_rud_view'),
    path('course/', CourseListCreateAPIView.as_view(), name='course_lc_view'),
    path('course/<int:pk__>', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course_rud_view'),
]
