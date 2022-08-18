from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('home/<str:pk>/',views.home,name="home"),
    path('create_project/',views.createProject,name="create_project"),
    path('update_project/<str:pk>/',views.updateProject,name="update_project"),
    path('delete_project/<str:pk>/',views.deleteProject,name="delete_project"),
    path('doctors/',views.doctor_view,name="doctors"),
    path('doctor_profile/<str:pk>/',views.doctor_profile,name="doctor_profile"),
 
]
