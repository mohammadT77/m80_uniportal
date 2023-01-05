from django.urls import path
from .views import *

urlpatterns = [
    path('semesters/', semester_view_list, name='semester_list'),
]
