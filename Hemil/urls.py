"""
URL configuration for Hemil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from soni import views

admin.site.site_header = "HEMIL'S Admin"
admin.site.site_title = "HEMIL'S Admin Portal"
admin.site.index_title = "Welcome to HEMIL Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('about/',views.aboutus),
    path('service/',views.service),
    path('contact/',views.contact),

]
