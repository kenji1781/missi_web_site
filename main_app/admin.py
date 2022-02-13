from django.contrib import admin
from .models import Customer_Infomation,Equipment_Category,Machine_Model,Trouble_Contents,\
    Unit_Price_Electric,Unit_Price_Steam,Unit_Price_Gas,Unit_Price_Water,Solvent_Name,Solvent_Manufacturer,\
        Solvent0_Conf,Solvent1_Conf,Solvent2_Conf,Solvent3_Conf,Solvent4_Conf,Solvent5_Conf,Solvent6_Conf,Solvent7_Conf,Solvent8_Conf,Solvent9_Conf,\
            Customer_Machine,Trouble_History,Customer_Machine_Recipe,Machine_Drive_History,\
                Cost_Electric,Cost_Steam,Cost_Gas,Cost_Water,Cost_Solvent,Cost_Total,Mail_Notification,\
                    Trouble_Mail_Setting,Maintenance_Mail_Setting,Setting_Item,Machine_Temperature_Log,Machine_Log,Plc_Output_Count_Log               


admin.site.register(Customer_Infomation)
admin.site.register(Equipment_Category)
admin.site.register(Machine_Model)
admin.site.register(Trouble_Contents)
admin.site.register(Unit_Price_Electric)
admin.site.register(Unit_Price_Steam)
admin.site.register(Unit_Price_Gas)
admin.site.register(Unit_Price_Water)
admin.site.register(Solvent_Name)
admin.site.register(Solvent_Manufacturer)
admin.site.register(Solvent0_Conf)
admin.site.register(Solvent1_Conf)
admin.site.register(Solvent2_Conf)
admin.site.register(Solvent3_Conf)
admin.site.register(Solvent4_Conf)
admin.site.register(Solvent5_Conf)
admin.site.register(Solvent6_Conf)
admin.site.register(Solvent7_Conf)
admin.site.register(Solvent8_Conf)
admin.site.register(Solvent9_Conf)
admin.site.register(Customer_Machine)
admin.site.register(Trouble_History)
admin.site.register(Customer_Machine_Recipe)
admin.site.register(Machine_Drive_History)
admin.site.register(Cost_Electric)
admin.site.register(Cost_Steam)
admin.site.register(Cost_Gas)
admin.site.register(Cost_Water)
admin.site.register(Cost_Solvent)
admin.site.register(Cost_Total)
admin.site.register(Mail_Notification)
admin.site.register(Trouble_Mail_Setting)
admin.site.register(Maintenance_Mail_Setting)
admin.site.register(Setting_Item)
admin.site.register(Machine_Temperature_Log)
admin.site.register(Machine_Log)
admin.site.register(Plc_Output_Count_Log)

# Register your models here.
