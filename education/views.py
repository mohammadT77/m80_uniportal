import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

from core.models import User
from education.models import Semester


def semester_view_list(request):
    semesters = Semester.objects.all()
    return render(request, 'education/semester_list.html', {'semesters': semesters})


def cookie_test_view(request, color: str = None):
    ccolor = request.COOKIES.get('color', None)  # Null
    resp = render(request, 'education/color_page.html', {'color': color or ccolor or 'white'})
    if color is not None:
        resp.set_cookie('color', color)
    return resp



from django.views import generic, View


class SemesterListView(generic.ListView):
    model = Semester
    context_object_name = 'semesters'
    template_name = 'education/semester_list.html'

    def get_queryset(self):
        return Semester.objects.filter(start_date__year=now().year)


class SimpleLoginView(View):
    def get(self, *args):
        return render(self.request, 'education/login.html' )

    def post(self, *args):
        username = self.request.POST['username']
        password = self.request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("User Not Found!")

        if user.check_password(password):
            return HttpResponse("OK")
        else:
            return HttpResponse("Incorrect password")
