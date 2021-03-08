from django.urls import path
from tango_with_django_project.rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name ='index'),
    path('about/', views.about, name ='about'),
]