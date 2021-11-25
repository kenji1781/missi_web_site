from django.urls import path,include
from django.contrib import admin
from .import views

app_name = 'main_app'
urlpatterns = [
    path('',views.index,name="index"),
    path('conf',views.conf,name="basic_conf"),
]
