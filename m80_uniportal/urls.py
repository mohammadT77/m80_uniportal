"""m80_uniportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from education.views import semester_view_list, SemesterListView, cookie_test_view, SimpleLoginView, api_test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('semesters/', semester_view_list, name='semester_list'), # func-based
    # path('semesters/', SemesterListView.as_view(), name='semester_list'), # class-based
    path('color/<str:color>', cookie_test_view),
    path('color/', cookie_test_view),
    # path('login/', SimpleLoginView.as_view(), name='login'),  # simple-login
    path('login/', LoginView.as_view(template_name='education/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('hello_world/', api_test_view),
]
