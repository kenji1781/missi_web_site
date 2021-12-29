from django.urls import path,include,re_path
from django.contrib import admin
from .views.index import IndexView
from .views.electric_price import ElectricPriceView,ElectricPriceCreateView,ElectricPriceUpdateView,ElectricPriceDeleteView
from .views.water_price import WaterPriceView,WaterPriceCreateView,WaterPriceUpdateView,WaterPriceDeleteView
from .views.steam_price import SteamPriceView,SteamPriceCreateView,SteamPriceUpdateView,SteamPriceDeleteView
from .views.gas_price import GasPriceView,GasPriceCreateView,GasPriceUpdateView,GasPriceDeleteView
from .views.solvent_name import SolventNameView,SolventNameCreateView,SolventNameUpdateView,SolventNameDeleteView
from .views.solvent_manufacturer import SolventManufacturerView,SolventManufacturerCreateView,SolventManufacturerUpdateView,SolventManufacturerDeleteView
from .views.solvent_conf import SolventConfView,SolventConfCreateView,SolventConfUpdateView,SolventConfDeleteView
from .views.equipment_category import EquipmentCategoryView,EquipmentCategoryCreateView,EquipmentCategoryUpdateView,EquipmentCategoryDeleteView
from .views.machine_model import MachineModelView,MachineModelCreateView,MachineModelUpdateView,MachineModelDeleteView
from .views.customer_machine import CustomerMachineView,CustomerMachineCreateView,CustomerMachineUpdateView,CustomerMachineDeleteView
from .views.customer_infomation import CustomerInfomationView,CustomerInfomationCreateView,CustomerInfomationUpdateView,CustomerInfomationDeleteView
from .views.trouble_contents import TroubleContentsView,TroubleContentsCreateView,TroubleContentsUpdateView,TroubleContentsDeleteView


app_name = 'main_app'
urlpatterns = [
    
    path('',IndexView.as_view(),name="index"),  #ホーム
    path('electricity_unit_price/',ElectricPriceView.as_view(),name="electric_price"),        #電力単価
    path('electricity_unit_price/create/',ElectricPriceCreateView.as_view(),name="electric_price_create"),   #電力単価
    path('electricity_unit_price/update/<int:pk>',ElectricPriceUpdateView.as_view(),name="electric_price_update"),   #電力単価
    path('electricity_unit_price/delete/<int:pk>',ElectricPriceDeleteView.as_view(),name="electric_price_delete"),       #電力単価
    path('water_unit_price/',WaterPriceView.as_view(),name="water_price"),        #水単価
    path('water_unit_price/create/',WaterPriceCreateView.as_view(),name="water_price_create"),   #水単価
    path('water_unit_price/update/<int:pk>',WaterPriceUpdateView.as_view(),name="water_price_update"),   #水単価
    path('water_unit_price/delete/<int:pk>',WaterPriceDeleteView.as_view(),name="water_price_delete"),   #水単価
    path('steam_unit_price/',SteamPriceView.as_view(),name="steam_price"),        #蒸気単価
    path('steam_unit_price/create/',SteamPriceCreateView.as_view(),name="steam_price_create"),   #蒸気単価
    path('steam_unit_price/update/<int:pk>',SteamPriceUpdateView.as_view(),name="steam_price_update"),   #蒸気単価
    path('steam_unit_price/delete/<int:pk>',SteamPriceDeleteView.as_view(),name="steam_price_delete"),   #蒸気単価
    path('gas_unit_price/',GasPriceView.as_view(),name="gas_price"),        #ガス単価
    path('gas_unit_price/create/',GasPriceCreateView.as_view(),name="gas_price_create"),   #ガス単価
    path('gas_unit_price/update/<int:pk>',GasPriceUpdateView.as_view(),name="gas_price_update"),   #ガス単価
    path('gas_unit_price/delete/<int:pk>',GasPriceDeleteView.as_view(),name="gas_price_delete"),   #ガス単価
    path('solvent_name/',SolventNameView.as_view(),name="solvent_name"),        #溶剤名
    path('solvent_name/create/',SolventNameCreateView.as_view(),name="solvent_name_create"),   #溶剤名
    path('solvent_name/update/<int:pk>',SolventNameUpdateView.as_view(),name="solvent_name_update"),   #溶剤名
    path('solvent_name/delete/<int:pk>',SolventNameDeleteView.as_view(),name="solvent_name_delete"),   #溶剤名
    path('solvent_manufacturer/',SolventManufacturerView.as_view(),name="solvent_manufacturer"),        #溶剤メーカ
    path('solvent_manufacturer/create/',SolventManufacturerCreateView.as_view(),name="solvent_manufacturer_create"),   #溶剤メーカ
    path('solvent_manufacturer/update/<int:pk>',SolventManufacturerUpdateView.as_view(),name="solvent_manufacturer_update"),   #溶剤メーカ
    path('solvent_manufacturer/delete/<int:pk>',SolventManufacturerDeleteView.as_view(),name="solvent_manufacturer_delete"),   #溶剤メーカ
    path('solvent_conf/',SolventConfView.as_view(),name="solvent_conf"),        #溶剤設定
    path('solvent_conf/create/',SolventConfCreateView.as_view(),name="solvent_conf_create"),   #溶剤設定
    path('solvent_conf/update/<int:pk>',SolventConfUpdateView.as_view(),name="solvent_conf_update"),   #溶剤設定
    path('solvent_conf/delete/<int:pk>',SolventConfDeleteView.as_view(),name="solvent_conf_delete"),   #溶剤設定
    path('equipment_category/',EquipmentCategoryView.as_view(),name="equipment_category"),        #装置カテゴリー
    path('equipment_category/create/',EquipmentCategoryCreateView.as_view(),name="equipment_category_create"),   #装置カテゴリー
    path('equipment_category/update/<int:pk>',EquipmentCategoryUpdateView.as_view(),name="equipment_category_update"),   #装置カテゴリー
    path('equipment_category/delete/<int:pk>',EquipmentCategoryDeleteView.as_view(),name="equipment_category_delete"),   #装置カテゴリー
    path('machine_model/',MachineModelView.as_view(),name="machine_model"),        #装置型式
    path('machine_model/create/',MachineModelCreateView.as_view(),name="machine_model_create"),   #装置型式
    path('machine_model/update/<int:pk>',MachineModelUpdateView.as_view(),name="machine_model_update"),   #装置型式
    path('machine_model/delete/<int:pk>',MachineModelDeleteView.as_view(),name="machine_model_delete"),   #装置型式
    path('customer_machine/',CustomerMachineView.as_view(),name="customer_machine"),        #装置型式
    path('customer_machine/create/',CustomerMachineCreateView.as_view(),name="customer_machine_create"),   #装置型式
    path('customer_machine/update/<int:pk>',CustomerMachineUpdateView.as_view(),name="customer_machine_update"),   #装置型式
    path('customer_machine/delete/<int:pk>',CustomerMachineDeleteView.as_view(),name="customer_machine_delete"),   #装置型式
    path('customer_infomation/',CustomerInfomationView.as_view(),name="customer_infomation"),        #客先情報
    path('customer_infomation/create/',CustomerInfomationCreateView.as_view(),name="customer_infomation_create"),   #客先情報
    path('customer_infomation/update/<int:pk>',CustomerInfomationUpdateView.as_view(),name="customer_infomation_update"),   #客先情報
    path('customer_infomation/delete/<int:pk>',CustomerInfomationDeleteView.as_view(),name="customer_infomation_delete"),   #客先情報
    path('trouble_contents/',TroubleContentsView.as_view(),name="trouble_contents"),        #異常
    path('trouble_contents/create/',TroubleContentsCreateView.as_view(),name="trouble_contents_create"),   #異常
    path('trouble_contents/update/<int:pk>',TroubleContentsUpdateView.as_view(),name="trouble_contents_update"),   #異常
    path('trouble_contents/delete/<int:pk>',TroubleContentsDeleteView.as_view(),name="trouble_contents_delete"),   #異常

    
    
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
