from django.urls import path
from . import views

app_name= 'home'

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name= 'contact'),
    path('enggCourse/', views.enggCourse, name='enggCourse'), 
    path('mmgCourse/', views.mmgCourse, name='mmgCourse'),
    path('medicalCourse/', views.medicalCourse, name='medicalCourse'),
    path('lawCourse/', views.lawCourse, name='lawCourse'),
    path('enggCollege/', views.enggCollege, name='enggCollege'), 
    path('mmgCollege/', views.mmgCollege, name='mmgCollege'),
    path('medicalCollege/', views.medicalCollege, name='medicalCollege'),
    path('lawCollege/', views.lawCollege, name='lawCollege'),
    path('<str:slug>/',views.EnggCollegeDetail, name='EnggCollegeDetail'),
]