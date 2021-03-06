"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home),

    path('adminclick', views.adminclick),
    path('studentclick', views.studentclick),


    path('adminsignup', views.adminsignup),
    path('studentsignup', views.studentsignup),
    path('adminlogin', LoginView.as_view(template_name='library/admin_login.html')),
    path('studentlogin', LoginView.as_view(template_name='library/student_login.html')),

    path('logout', LogoutView.as_view(template_name='library/main_page.html')),
    path('afterlogin', views.afterlogin),

    path('addbook', views.addbook),
    path('viewbook', views.viewbook),
    path('issuebook', views.issuebook),
    path('viewissuedbook', views.viewissuedbook),
    path('viewstudent', views.viewstudent),
    path('viewissuedbookbystudent', views.view_issued_book_student),

    path('aboutus', views.aboutus),
    path('contactus', views.contactus),

]
