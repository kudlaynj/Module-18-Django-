"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import index, Index2
from task4.views import task3_1, task3_2, task3_3, task3_4, menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', index),
    path('class/', Index2.as_view()),
    path('platform/', task3_1),
    path('methmat/', task3_3),
    path('services/', task3_2),
    path('cart/', task3_4),
    path('menu/', menu),
    path('reg/', sign_up_by_django),
    path('registration/', sign_up_by_html),
]
