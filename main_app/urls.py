from django.urls import path,include
from django.contrib import admin
from .import views

app_name = 'main_app'
urlpatterns = [
    path('',views.index,name="index"),  #ホーム
    path('electric_price/',views.conf,name="electric_price"),    #電力単価
    path('water_price/',views.conf,name="water_price"),    #水単価    
    path('steam_price/',views.conf,name="steam_price"),   #蒸気単価
    path('gas_price/',views.conf,name="gas_price"),    #ガス単価
    path('solvent_price/',views.conf,name="solvent_price"),    #溶剤単価
    path('device/',views.conf,name="device"),    #装置
    path('recipe_setting/',views.conf,name="recipe_setting"),    #品種設定
    path('registering_email/',views.conf,name="registering_email"),    #通知メール登録
    path('trouble_email/',views.conf,name="trouble_email"),    #異常メール設定
    path('maintenance_email/',views.conf,name="meintenance_email"),    #メンテナンスメール設定
    path('recipe_infomation/',views.conf,name="recipe_infomation"),    #レシピ情報
    path('drive_history/',views.conf,name="drive_history"),    #稼働履歴
    path('trouble_history/',views.conf,name="trouble_history"),    #異常履歴
    path('electric_cost/',views.conf,name="electric_cost"),    #電力コスト
    path('water_cost/',views.conf,name="water_cost"),    #水コスト
    path('steam_cost/',views.conf,name="steam_cost"),    #蒸気コスト
    path('gas_cost/',views.conf,name="gas_cost"),    #ガスコスト
    path('solvent_cost/',views.conf,name="solvent_cost"),    #溶剤コスト
    path('total_cost/',views.conf,name="total_cost"),    #トータルコスト
    path('customer_infomation/',views.conf,name="customer_infomation"),    #客先情報
    path('machine_category/',views.conf,name="machine_category"),    #装置カテゴリー
    path('machine_model/',views.conf,name="machine_model"),    #装置型式
]
