from django.http import JsonResponse
from rest_framework import generics
from education.models import Semester
from education.serializers import SemesterSerializer


def semester_list_api(request):
    semesters = Semester.objects.all()  # list -> many=true
    semesters_serialized = SemesterSerializer(data=..., many=True)
    return JsonResponse({'semesters': semesters_serialized})


class SemesterListApi(generics.ListAPIView):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()
