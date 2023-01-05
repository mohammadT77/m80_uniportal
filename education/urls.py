from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path("", TemplateView.as_view(template_name='education/index.html'), name='education_index'),
    path('semesters/', semester_view_list, name='semester_list'),
]
