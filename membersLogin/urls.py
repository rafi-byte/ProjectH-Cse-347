from xml.etree.ElementInclude import include
from django.urls import path
from membersLogin.views import UserRegisterView
# from .views import UserRegisterView, HomeView, articleview,UpdatePostView,DeletePostView
# from Healthcare.projects import admin

urlpatterns=[

 path('registers/',UserRegisterView.as_view(),name='registers'),


]