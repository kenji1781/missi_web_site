from django.urls import path,include
from django.contrib import admin
from .import views

app_name = 'main_app'
urlpatterns = [
    path('',views.index,name="index"),  #ホーム
    path('basic_conf',views.conf,name="basic_conf"),    #基本設定
    path('basic_conf',views.conf,name="basic_conf"),    #基本設定-
    path('machine_info',views.conf,name="machine_info"),   #装置情報
    path('manufacturer',views.conf,name="manufacturer"),    #メーカー設定
    path('manufacturer/customer_info',views.conf,name="customer_info"),    #客先情報
    path('manufacturer/equipment_category',views.conf,name="equipment_category"),    #装置カテゴリー
    path('manufacturer/machine_model',views.conf,name="machine_model"),    #装置型式
]
