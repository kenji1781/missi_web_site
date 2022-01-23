from django.urls import path,include,re_path
from django.contrib import admin
from .views.index import IndexView
from .views.electric_price import ElectricPriceView,ElectricPriceCreateView,ElectricPriceUpdateView,ElectricPriceDeleteView
from .views.water_price import WaterPriceView,WaterPriceCreateView,WaterPriceUpdateView,WaterPriceDeleteView
from .views.steam_price import SteamPriceView,SteamPriceCreateView,SteamPriceUpdateView,SteamPriceDeleteView
from .views.gas_price import GasPriceView,GasPriceCreateView,GasPriceUpdateView,GasPriceDeleteView
from .views.solvent_name import SolventNameView,SolventNameCreateView,SolventNameUpdateView,SolventNameDeleteView
from .views.solvent_manufacturer import SolventManufacturerView,SolventManufacturerCreateView,SolventManufacturerUpdateView,SolventManufacturerDeleteView
from .views.solvent0_conf import Solvent0ConfView,Solvent0ConfCreateView,Solvent0ConfUpdateView,Solvent0ConfDeleteView
from .views.solvent1_conf import Solvent1ConfView,Solvent1ConfCreateView,Solvent1ConfUpdateView,Solvent1ConfDeleteView
from .views.solvent2_conf import Solvent2ConfView,Solvent2ConfCreateView,Solvent2ConfUpdateView,Solvent2ConfDeleteView
from .views.solvent3_conf import Solvent3ConfView,Solvent3ConfCreateView,Solvent3ConfUpdateView,Solvent3ConfDeleteView
from .views.solvent4_conf import Solvent4ConfView,Solvent4ConfCreateView,Solvent4ConfUpdateView,Solvent4ConfDeleteView
from .views.solvent5_conf import Solvent5ConfView,Solvent5ConfCreateView,Solvent5ConfUpdateView,Solvent5ConfDeleteView
from .views.solvent6_conf import Solvent6ConfView,Solvent6ConfCreateView,Solvent6ConfUpdateView,Solvent6ConfDeleteView
from .views.solvent7_conf import Solvent7ConfView,Solvent7ConfCreateView,Solvent7ConfUpdateView,Solvent7ConfDeleteView
from .views.solvent8_conf import Solvent8ConfView,Solvent8ConfCreateView,Solvent8ConfUpdateView,Solvent8ConfDeleteView
from .views.solvent9_conf import Solvent9ConfView,Solvent9ConfCreateView,Solvent9ConfUpdateView,Solvent9ConfDeleteView

from .views.equipment_category import EquipmentCategoryView,EquipmentCategoryCreateView,EquipmentCategoryUpdateView,EquipmentCategoryDeleteView
from .views.machine_model import MachineModelView,MachineModelCreateView,MachineModelUpdateView,MachineModelDeleteView
from .views.customer_machine import CustomerMachineView,CustomerMachineCreateView,CustomerMachineUpdateView,CustomerMachineDeleteView
from .views.customer_infomation import CustomerInfomationView,CustomerInfomationCreateView,CustomerInfomationUpdateView,CustomerInfomationDeleteView
from .views.trouble_contents import TroubleContentsView,TroubleContentsCreateView,TroubleContentsUpdateView,TroubleContentsDeleteView
from .views.trouble_history import TroubleHistoryView,TroubleHistoryCreateView,TroubleHistoryUpdateView,TroubleHistoryDeleteView
from .views.setting_item import SettingItemView,SettingItemCreateView,SettingItemUpdateView,SettingItemDeleteView
from .views.customer_machine_recipe import CustomerMachineRecipeView,CustomerMachineRecipeCreateView,CustomerMachineRecipeUpdateView,CustomerMachineRecipeDeleteView
from .views.machine_drive_history import MachineDriveHistoryView,MachineDriveHistoryCreateView,MachineDriveHistoryUpdateView,MachineDriveHistoryDeleteView
from .views.cost_electric import CostElectricView
from .views.cost_steam import CostSteamView
from .views.cost_gas import CostGasView
from .views.cost_water import CostWaterView
from .views.cost_solvent0 import CostSolvent0View
from .views.cost_solvent1 import CostSolvent1View
from .views.cost_solvent2 import CostSolvent2View
from .views.cost_solvent3 import CostSolvent3View
from .views.cost_solvent4 import CostSolvent4View
from .views.cost_solvent5 import CostSolvent5View
from .views.cost_solvent6 import CostSolvent6View
from .views.cost_solvent7 import CostSolvent7View
from .views.cost_solvent8 import CostSolvent8View
from .views.cost_solvent9 import CostSolvent9View

from .views.cost_electric_graph import CostElectricGraphView
from .views.cost_steam_graph import CostSteamGraphView
from .views.cost_gas_graph import CostGasGraphView
from .views.cost_water_graph import CostWaterGraphView
from .views.cost_solvent0_graph import CostSolvent0GraphView
from .views.cost_solvent1_graph import CostSolvent1GraphView
from .views.cost_solvent2_graph import CostSolvent2GraphView
from .views.cost_solvent3_graph import CostSolvent3GraphView
from .views.cost_solvent4_graph import CostSolvent4GraphView
from .views.cost_solvent5_graph import CostSolvent5GraphView
from .views.cost_solvent6_graph import CostSolvent6GraphView
from .views.cost_solvent7_graph import CostSolvent7GraphView
from .views.cost_solvent8_graph import CostSolvent8GraphView
from .views.cost_solvent9_graph import CostSolvent9GraphView
from .views.cost_solvent9_graph import CostSolvent9GraphView
#from .views.cost_solvent9_graph import CostSolvent9GraphView


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
    path('solvent0_conf/',Solvent0ConfView.as_view(),name="solvent0_conf"),        #溶剤0設定
    path('solvent0_conf/create/',Solvent0ConfCreateView.as_view(),name="solvent0_conf_create"),   #溶剤0設定
    path('solvent0_conf/update/<int:pk>',Solvent0ConfUpdateView.as_view(),name="solvent0_conf_update"),   #溶剤0設定
    path('solvent0_conf/delete/<int:pk>',Solvent0ConfDeleteView.as_view(),name="solvent0_conf_delete"),   #溶剤0設定
    path('solvent1_conf/',Solvent1ConfView.as_view(),name="solvent1_conf"),        #溶剤1設定
    path('solvent1_conf/create/',Solvent1ConfCreateView.as_view(),name="solvent1_conf_create"),   #溶剤1設定
    path('solvent1_conf/update/<int:pk>',Solvent1ConfUpdateView.as_view(),name="solvent1_conf_update"),   #溶剤1設定
    path('solvent1_conf/delete/<int:pk>',Solvent1ConfDeleteView.as_view(),name="solvent1_conf_delete"),   #溶剤1設定
    path('solvent2_conf/',Solvent2ConfView.as_view(),name="solvent2_conf"),        #溶剤2設定
    path('solvent2_conf/create/',Solvent2ConfCreateView.as_view(),name="solvent2_conf_create"),   #溶剤2設定
    path('solvent2_conf/update/<int:pk>',Solvent2ConfUpdateView.as_view(),name="solvent2_conf_update"),   #溶剤2設定
    path('solvent2_conf/delete/<int:pk>',Solvent2ConfDeleteView.as_view(),name="solvent2_conf_delete"),   #溶剤2設定
    path('solvent3_conf/',Solvent3ConfView.as_view(),name="solvent3_conf"),        #溶剤3設定
    path('solvent3_conf/create/',Solvent3ConfCreateView.as_view(),name="solvent3_conf_create"),   #溶剤3設定
    path('solvent3_conf/update/<int:pk>',Solvent3ConfUpdateView.as_view(),name="solvent3_conf_update"),   #溶剤3設定
    path('solvent3_conf/delete/<int:pk>',Solvent3ConfDeleteView.as_view(),name="solvent3_conf_delete"),   #溶剤3設定
    path('solvent4_conf/',Solvent4ConfView.as_view(),name="solvent4_conf"),        #溶剤4設定
    path('solvent4_conf/create/',Solvent4ConfCreateView.as_view(),name="solvent4_conf_create"),   #溶剤4設定
    path('solvent4_conf/update/<int:pk>',Solvent4ConfUpdateView.as_view(),name="solvent4_conf_update"),   #溶剤4設定
    path('solvent4_conf/delete/<int:pk>',Solvent4ConfDeleteView.as_view(),name="solvent4_conf_delete"),   #溶剤4設定
    path('solvent5_conf/',Solvent5ConfView.as_view(),name="solvent5_conf"),        #溶剤5設定
    path('solvent5_conf/create/',Solvent5ConfCreateView.as_view(),name="solvent5_conf_create"),   #溶剤5設定
    path('solvent5_conf/update/<int:pk>',Solvent5ConfUpdateView.as_view(),name="solvent5_conf_update"),   #溶剤5設定
    path('solvent5_conf/delete/<int:pk>',Solvent5ConfDeleteView.as_view(),name="solvent5_conf_delete"),   #溶剤5設定
    path('solvent6_conf/',Solvent6ConfView.as_view(),name="solvent6_conf"),        #溶剤6設定
    path('solvent6_conf/create/',Solvent6ConfCreateView.as_view(),name="solvent6_conf_create"),   #溶剤6設定
    path('solvent6_conf/update/<int:pk>',Solvent6ConfUpdateView.as_view(),name="solvent6_conf_update"),   #溶剤6設定
    path('solvent6_conf/delete/<int:pk>',Solvent6ConfDeleteView.as_view(),name="solvent6_conf_delete"),   #溶剤6設定
    path('solvent7_conf/',Solvent7ConfView.as_view(),name="solvent7_conf"),        #溶剤7設定
    path('solvent7_conf/create/',Solvent7ConfCreateView.as_view(),name="solvent7_conf_create"),   #溶剤7設定
    path('solvent7_conf/update/<int:pk>',Solvent7ConfUpdateView.as_view(),name="solvent7_conf_update"),   #溶剤7設定
    path('solvent7_conf/delete/<int:pk>',Solvent7ConfDeleteView.as_view(),name="solvent7_conf_delete"),   #溶剤7設定
    path('solvent8_conf/',Solvent8ConfView.as_view(),name="solvent8_conf"),        #溶剤8設定
    path('solvent8_conf/create/',Solvent8ConfCreateView.as_view(),name="solvent8_conf_create"),   #溶剤8設定
    path('solvent8_conf/update/<int:pk>',Solvent8ConfUpdateView.as_view(),name="solvent8_conf_update"),   #溶剤8設定
    path('solvent8_conf/delete/<int:pk>',Solvent8ConfDeleteView.as_view(),name="solvent8_conf_delete"),   #溶剤8設定
    path('solvent9_conf/',Solvent9ConfView.as_view(),name="solvent9_conf"),        #溶剤9設定
    path('solvent9_conf/create/',Solvent9ConfCreateView.as_view(),name="solvent9_conf_create"),   #溶剤9設定
    path('solvent9_conf/update/<int:pk>',Solvent9ConfUpdateView.as_view(),name="solvent9_conf_update"),   #溶剤9設定
    path('solvent9_conf/delete/<int:pk>',Solvent9ConfDeleteView.as_view(),name="solvent9_conf_delete"),   #溶剤9設定
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
    path('trouble_history/',TroubleHistoryView.as_view(),name="trouble_history"),        #異常履歴
    path('trouble_history/create/',TroubleHistoryCreateView.as_view(),name="trouble_history_create"),   #異常履歴
    path('trouble_history/update/<int:pk>',TroubleHistoryUpdateView.as_view(),name="trouble_history_update"),   #異常履歴
    path('trouble_history/delete/<int:pk>',TroubleHistoryDeleteView.as_view(),name="trouble_history_delete"),   #異常履歴
    path('setting_item/',SettingItemView.as_view(),name="setting_item"),        #品種
    path('setting_item/create/',SettingItemCreateView.as_view(),name="setting_item_create"),   #品種
    path('setting_item/update/<int:pk>',SettingItemUpdateView.as_view(),name="setting_item_update"),   #品種
    path('setting_item/delete/<int:pk>',SettingItemDeleteView.as_view(),name="setting_item_delete"),   #品種
    path('customer_machine_recipe/',CustomerMachineRecipeView.as_view(),name="customer_machine_recipe"),        #レシピ
    path('customer_machine_recipe/create/',CustomerMachineRecipeCreateView.as_view(),name="customer_machine_recipe_create"),   #レシピ
    path('customer_machine_recipe/update/<int:pk>',CustomerMachineRecipeUpdateView.as_view(),name="customer_machine_recipe_update"),   #レシピ
    path('customer_machine_recipe/delete/<int:pk>',CustomerMachineRecipeDeleteView.as_view(),name="customer_machine_recipe_delete"),   #レシピ
    path('machine_drive_history/',MachineDriveHistoryView.as_view(),name="machine_drive_history"),        #稼働履歴
    path('machine_drive_history/create/',MachineDriveHistoryCreateView.as_view(),name="machine_drive_history_create"),   #稼働履歴
    path('machine_drive_history/update/<int:pk>',MachineDriveHistoryUpdateView.as_view(),name="machine_drive_history_update"),   #稼働履歴
    path('machine_drive_history/delete/<int:pk>',MachineDriveHistoryDeleteView.as_view(),name="machine_drive_history_delete"),   #稼働履歴
    path('cost_electric/',CostElectricView.as_view(),name="cost_electric"),        #電力コスト
    path('cost_steam/',CostGasView.as_view(),name="cost_steam"),        #蒸気コスト
    path('cost_gas/',CostGasView.as_view(),name="cost_gas"),        #ガスコスト
    path('cost_water/',CostWaterView.as_view(),name="cost_water"),        #水コスト
    path('cost_solvent0/',CostSolvent0View.as_view(),name="cost_solvent0"),        #溶剤＊コスト
    path('cost_solvent1/',CostSolvent1View.as_view(),name="cost_solvent1"),        #溶剤＊コスト
    path('cost_solvent2/',CostSolvent2View.as_view(),name="cost_solvent2"),        #溶剤＊コスト
    path('cost_solvent3/',CostSolvent3View.as_view(),name="cost_solvent3"),        #溶剤＊コスト
    path('cost_solvent4/',CostSolvent4View.as_view(),name="cost_solvent4"),        #溶剤＊コスト
    path('cost_solvent5/',CostSolvent5View.as_view(),name="cost_solvent5"),        #溶剤＊コスト
    path('cost_solvent6/',CostSolvent6View.as_view(),name="cost_solvent6"),        #溶剤＊コスト
    path('cost_solvent7/',CostSolvent7View.as_view(),name="cost_solvent7"),        #溶剤＊コスト
    path('cost_solvent8/',CostSolvent8View.as_view(),name="cost_solvent8"),        #溶剤＊コスト
    path('cost_solvent9/',CostSolvent9View.as_view(),name="cost_solvent9"),        #溶剤＊コスト
    
    path('cost_electric_graph/<int:year>/<int:month>/',CostElectricGraphView.as_view(),name="cost_electric_graph"),   #電力コストグラフ
    path('cost_steam_graph/<int:year>/<int:month>/',CostSteamGraphView.as_view(),name="cost_steam_graph"),   #蒸気コストグラフ
    path('cost_gas_graph/<int:year>/<int:month>/',CostGasGraphView.as_view(),name="cost_gas_graph"),   #ガスコストグラフ
    path('cost_water_graph/<int:year>/<int:month>/',CostWaterGraphView.as_view(),name="cost_water_graph"),   #水コストグラフ
    path('cost_solvent0_graph/<int:year>/<int:month>/',CostSolvent0GraphView.as_view(),name="cost_solvent0_graph"),   #溶剤0コストグラフ
    path('cost_solvent1_graph/<int:year>/<int:month>/',CostSolvent1GraphView.as_view(),name="cost_solvent1_graph"),   #溶剤0コストグラフ
    path('cost_solvent2_graph/<int:year>/<int:month>/',CostSolvent2GraphView.as_view(),name="cost_solvent2_graph"),   #溶剤0コストグラフ
    path('cost_solvent3_graph/<int:year>/<int:month>/',CostSolvent3GraphView.as_view(),name="cost_solvent3_graph"),   #溶剤0コストグラフ
    path('cost_solvent4_graph/<int:year>/<int:month>/',CostSolvent4GraphView.as_view(),name="cost_solvent4_graph"),   #溶剤0コストグラフ
    path('cost_solvent5_graph/<int:year>/<int:month>/',CostSolvent5GraphView.as_view(),name="cost_solvent5_graph"),   #溶剤0コストグラフ
    path('cost_solvent6_graph/<int:year>/<int:month>/',CostSolvent6GraphView.as_view(),name="cost_solvent6_graph"),   #溶剤0コストグラフ
    path('cost_solvent7_graph/<int:year>/<int:month>/',CostSolvent7GraphView.as_view(),name="cost_solvent7_graph"),   #溶剤0コストグラフ
    path('cost_solvent8_graph/<int:year>/<int:month>/',CostSolvent8GraphView.as_view(),name="cost_solvent8_graph"),   #溶剤0コストグラフ
    path('cost_solvent9_graph/<int:year>/<int:month>/',CostSolvent9GraphView.as_view(),name="cost_solvent9_graph"),   #溶剤0コストグラフ
    #path('trouble_history_graph/<int:year>/<int:month>/',TroubleHistoryGraphView.as_view(),name="trouble_history_graph"),   #異常グラフ
    
    ]
