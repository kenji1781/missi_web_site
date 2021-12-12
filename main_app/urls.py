from django.urls import path,include
from django.contrib import admin
from .views import IndexView,ElectricPriceView,ElectricPriceCreateView

app_name = 'main_app'
urlpatterns = [
    path('',IndexView.as_view(),name="index"),  #ホーム
    path('electricity_unit_price/',ElectricPriceView.as_view(),name="electric_price"),        #電力単価
    path('electricity_unit_price/create/',ElectricPriceCreateView.as_view(),name="electric_price_create"),        #電力単価
    #path('water_price/',views.water_price,name="water_price"),    #水単価    
    #path('steam_price/',views.steam_price,name="steam_price"),   #蒸気単価
    #path('gas_price/',views.gas_price,name="gas_price"),    #ガス単価
    #path('solvent_price/',views.solvent_price,name="solvent_price"),    #溶剤単価
    #path('device/',views.device,name="device"),    #装置
    #path('recipe_setting/',views.recipe_setting,name="recipe_setting"),    #品種設定
    #path('registering_email/',views.registering_email,name="registering_email"),    #通知メール登録
    #path('trouble_email/',views.trouble_email,name="trouble_email"),    #異常メール設定
    #path('maintenance_email/',views.maintenance_email,name="maintenance_email"),    #メンテナンスメール設定
    #path('recipe_infomation/',views.recipe_infomation,name="recipe_infomation"),    #レシピ情報
    #path('drive_history/',views.drive_history,name="drive_history"),    #稼働履歴
    #path('trouble_history/',views.trouble_history,name="trouble_history"),    #異常履歴
    #path('electric_cost/',views.electric_cost,name="electric_cost"),    #電力コスト
    #path('water_cost/',views.water_cost,name="water_cost"),    #水コスト
    #path('steam_cost/',views.steam_cost,name="steam_cost"),    #蒸気コスト
    #path('gas_cost/',views.gas_cost,name="gas_cost"),    #ガスコスト
    #path('solvent_cost/',views.solvent_cost,name="solvent_cost"),    #溶剤コスト
    #path('total_cost/',views.total_cost,name="total_cost"),    #トータルコスト
    #path('customer_infomation/',views.customer_infomation,name="customer_infomation"),    #客先情報
    #path('machine_category/',views.machine_category,name="machine_category"),    #装置カテゴリー
    #path('machine_model/',views.machine_model,name="machine_model"),    #装置型式
]
