"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/',views.show,name='addandshow'),
    path('delete/<int:id>/',views.deletedate,name='deletedata'),
    path('<int:id>/',views.update,name='updatedata'),
    path('', views.userregistration,name="register"),
    path("login/",views.user_login, name="login"),
    path('logout',views.user_logout,name='logout'),
    path('adminupdate<int:id>/',views.adminupdate,name='adminupdate'),
    path('delete<int:id>/',views.admindelete,name='admindelete'),
    # path("fm",views.flormregistration,name='fmregister'),
    # path("tl",views.teamleadregistration,name='tlregister'),
    # path("tm",views.teammregistration,name='tmregister'),
    path("detailsdata/",views.detailsdata,name='detailsdata'),

    # path("dashboard",views.dashboard,name='dashboard'),



]
