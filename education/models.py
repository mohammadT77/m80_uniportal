from django.db import models

# Create your models here.
from django.utils.translation import gettext as _

from core.models import BaseModel, User


class Department(BaseModel):
    pass


class Student(User):
    age = models.IntegerField(_("Age"))
    dept = models.ForeignKey(Department, on_delete=models.RESTRICT, verbose_name=_("Department"), null=False)
    degree = models.ForeignKey("Degree", on_delete=models.RESTRICT, verbose_name=_("Degree"), null=False)
    courses = models.ManyToManyField("Course", verbose_name=_("Courses"), blank=True)


class Professor(User):
    dept = models.ForeignKey(Department, on_delete=models.RESTRICT, verbose_name=_("Department"))


class Course(BaseModel):
    exam_date = models.DateTimeField(_("Exam date"))
    name = models.CharField(_("Course name"), max_length=20)

    semester = models.ForeignKey("Semester", on_delete=models.RESTRICT, verbose_name=_("Semester"))
    dept = models.ForeignKey("Department", on_delete=models.RESTRICT, verbose_name=_("Department"))
    prof = models.ForeignKey("Professor", on_delete=models.RESTRICT, verbose_name=_("Professor"))
    degree = models.ForeignKey("Degree", on_delete=models.RESTRICT, verbose_name=_("Degree"))


class Semester(BaseModel):
    start_date = models.DateField(_("Start date"))
    end_date = models.DateField(_("End date"))


class Degree(BaseModel):
    level = models.CharField(_("Level"), choices=[
        ("B", _("Bachelor")),
        ("M", _("Master")),
        ("D", _("PhD")),
    ], max_length=1)
    track = models.CharField(_("Track"), max_length=20)
