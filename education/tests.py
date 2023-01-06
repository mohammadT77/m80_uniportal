from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class SemesterViewTest(TestCase):
    def test1_get_semesters_list(self):
        client = APIClient(enforce_csrf_checks=False)
        client.login(username='student1', password='AkbarRezaii1234')

        resp = client.get('/api/education/semester/')
        print(dir(resp))
        print(resp.data)
        print(resp.content)