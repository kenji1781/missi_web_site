from django import forms
from django.forms import fields, models,widgets
from .models import Customer_Infomation,Equipment_Category,Machine_Model,Trouble_Contents,\
    Unit_Price_Electric,Unit_Price_Steam,Unit_Price_Gas,Unit_Price_Water,Solvent_Name,Solvent_Manufacturer,Solvent_Conf,\
        Customer_Machine,Trouble_History,Customer_Machine_Recipe,Machine_Drive_History,\
            Cost_Electric,Cost_Steam,Cost_Gas,Cost_Water,Cost_Solvent,Cost_Total


class DateInput(forms.DateInput):
    input_type = 'date'


class ElectricPriceCreateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Electric
        fields = ('Unit_price_electric','Unit_price_electric_input_date','Unit_price_electric_memo')
        widgets = {
            'Unit_price_electric_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_electric':'単価：（￥）',
                    'Unit_price_electric_input_date':'登録日',
                    'Unit_price_electric_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_electric'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_electric_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_electric_memo'].widgets.attrs["class"] = "form-control"


class ElectricPriceUpdateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Electric
        fields = ('Unit_price_electric','Unit_price_electric_input_date','Unit_price_electric_memo')
        widgets = {
            'Unit_price_electric_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_electric':'単価：（￥）',
                    'Unit_price_electric_input_date':'登録日',
                    'Unit_price_electric_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_electric'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_electric_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_electric_memo'].widgets.attrs["class"] = "form-control"





class customer_infomation(forms.ModelForm):
    class Meta:
        models = Customer_Infomation
        fields = '__all__'
        Labels = {  
                    'Customer_name':'企業名',
                    'Customer_tel_number':'Tel',
                    'Customer_pastal_code':'〒',
                    'Customer_address1':'都道府県',
                    'Customer_address2':'市町村',
                    'Customer_address3':'建物名',
                    'Customer_input_date':'登録日',
                    'Customer_memo':'メモ'
                    }



class equipment_category(forms.ModelForm):
    class Meta:
        models = Equipment_Category
        fields = '__all__'
        Labels = {  
                    'Equipment_category':'装置カテゴリー'
                    }




class machine_model(forms.ModelForm):
    class Meta:
        models = Machine_Model
        fields = '__all__'
        
        Labels = {  
                    'Machine_category':'装置カテゴリー',
                    'Machine_model':'型式',
                    'Machine_model_input_date':'登録日',
                    'Machine_model_memo':'メモ'
                    }




class trouble_contents(forms.ModelForm):
    class Meta:
        models = Trouble_Contents
        fields = '__all__'
        Labels = {  
                    'Machine_model':'装置',
                    'Trouble_no':'異常No',
                    'Trouble_contents':'異常',
                    'Trouble_input_date':'登録日',
                    'Trouble_memo':'メモ'
                    }



class unit_price_electric(forms.ModelForm):
    class Meta:
        models = Unit_Price_Electric
        fields = '__all__'
        Labels = {  
                    'Unit_price_electric':'単価',
                    'Unit_price_electric_input_date':'登録日',
                    'Unit_price_electric_memo':'メモ'
                    }



class unit_price_steam(forms.ModelForm):
    class Meta:
        models = Unit_Price_Steam
        fields = '__all__'
        Labels = {  
                    'Unit_price_steam':'単価',
                    'Unit_price_steam_input_date':'登録日',
                    'Unit_price_steam_memo':'メモ'
                    }



class unit_price_gas(forms.ModelForm):
    class Meta:
        models = Unit_Price_Gas
        fields = '__all__'
        Labels = {  
                    'Unit_price_gas':'単価',
                    'Unit_price_gas_input_date':'登録日',
                    'Unit_price_gas_memo':'メモ'
                    }




class unit_price_water(forms.ModelForm):
    class Meta:
        models = Unit_Price_Water
        fields = '__all__'
        Labels = {  
                    'Unit_price_water':'単価',
                    'Unit_price_water_input_date':'登録日',
                    'Unit_price_water_memo':'メモ'
                    }



class solvent_name(forms.ModelForm):
    class Meta:
        models = Solvent_Name
        fields = '__all__'
        Labels = {  
                    'Solvent_name':'溶剤名'
                    }




class solvent_manufacturer(forms.ModelForm):
    class Meta:
        models = Solvent_Manufacturer
        fields = '__all__'
        Labels = {  
                    'Solvent_name':'溶剤名',
                    'Solvent_manu':'メーカー'
                    }



class solvent_conf(forms.ModelForm):
    class Meta:
        models = Solvent_Conf
        fields = '__all__'
        Labels = {  
                    'Solvent_manu':'溶剤名',
                    'Solvent_unit_price':'単価',
                    'Solvent_input_date':'登録日',
                    'Solvent_memo':'メモ'
                    }




class customer_machine(forms.ModelForm):
    class Meta:
        models = Customer_Machine
        fields = '__all__'
        Labels = {  
                    'Machine_model':'装置',
                    'Customer_machine_unit_no':'製番',
                    'Customer_machine_inst_date':'納入日',
                    'Customer_machine_input_date':'登録日',
                    'Customer_machine_memo':'メモ'
                    }



class trouble_history(forms.ModelForm):
    class Meta:
        models = Trouble_History
        fields = '__all__'
        Labels = {  
                    'Customer_machine':'装置',
                    'Trouble_contents':'異常',
                    'Trouble_occurrence_time':'発生時刻',
                    'Trouble_recovery_time':'復帰時刻'
                    }




class customer_machine_recipe(forms.ModelForm):
    class Meta:
        models = Customer_Machine_Recipe
        fields = '__all__'
        Labels = {  
                    'Customer_machine':'装置',
                    'Customer_recipe_no':'品種No',
                    'Customer_recipe_name':'品種名',
                    'Customer_recipe_time':'運転時間',
                    'Customer_recipe_time1':'乾燥時間1',
                    'Customer_recipe_time2':'乾燥時間2',
                    'Customer_recipe_time3':'乾燥時間3',
                    'Customer_recipe_time4':'乾燥時間4',
                    'Customer_recipe_temp1':'温度設定1',
                    'Customer_recipe_temp2':'温度設定2',
                    'Customer_recipe_temp3':'温度設定3',
                    'Customer_recipe_temp4':'温度設定4',
                    'Customer_recipe_conf1':'設定1',
                    'Customer_recipe_conf2':'設定2',
                    'Customer_recipe_conf3':'設定3',
                    'Customer_recipe_conf4':'設定4',
                    'Customer_recipe_conf5':'設定5',
                    'Customer_recipe_conf6':'設定6',
                    'Customer_machine_input_date':'登録日',
                    'Customer_machine_memo':'メモ'
                    }




class machine_drive_history(forms.ModelForm):
    class Meta:
        models = Machine_Drive_History
        fields = (
                    'Customer_machine_recipe',
                    'Machine_drying_time',
                    'Machine_drive_count',
                    'Machine_steam_used',
                    'Machine_electric_used',
                    'Machine_gas_used',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = {  
                    'Customer_machine_recipe':'品種',
                    'Machine_drying_time':'乾燥時間',
                    'Machine_drive_count':'稼働回数',
                    'Machine_steam_used':'蒸気使用量',
                    'Machine_electric_used':'電力使用量',
                    'Machine_gas_used':'ガス使用量',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }
    

class cost_electric(forms.ModelForm):
    class Meta:
        models = Cost_Electric
        fields = (        
                    'Machine_drive_history',
                    'Unit_price_electric',
                    'Cost_electric',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = { 
                    'Machine_drive_history':'稼働履歴',
                    'Unit_price_electric':'電力単価',
                    'Cost_electric':'電力費用',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }



class cost_steam(forms.ModelForm):
    class Meta:
        models = Cost_Steam
        fields = (        
                    'Machine_drive_history',
                    'Unit_price_steam',
                    'Cost_steam',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = { 
                    'Machine_drive_history':'稼働履歴',
                    'Unit_price_steam':'蒸気単価',
                    'Cost_steam':'蒸気費用',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }



class cost_gas(forms.ModelForm):
    class Meta:
        models = Cost_Gas
        fields = (        
                    'Machine_drive_history',
                    'Unit_price_gas',
                    'Cost_gas',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = { 
                    'Machine_drive_history':'稼働履歴',
                    'Unit_price_gas':'ガス単価',
                    'Cost_gas':'ガス費用',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }



class cost_water(forms.ModelForm):
    class Meta:
        models = Cost_Water
        fields = (        
                    'Machine_drive_history',
                    'Unit_price_water',
                    'Cost_water',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = { 
                    'Machine_drive_history':'稼働履歴',
                    'Unit_price_water':'水単価',
                    'Cost_water':'水費用',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }



class cost_solvent(forms.ModelForm):
    class Meta:
        models = Cost_Solvent
        fields = (        
                    'Machine_drive_history',
                    'Unit_price_solvent',
                    'Cost_solvent',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = { 
                    'Machine_drive_history':'稼働履歴',
                    'Unit_price_solvent':'溶剤単価',
                    'Cost_solvent':'溶剤費用',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }







class cost_total(forms.ModelForm):
    class Meta:
        models = Cost_Total
        fields = (        
                    'Machine_drive_history',
                    'Cost_electric',
                    'Cost_steam',
                    'Cost_gas',
                    'Cost_water',
                    'Cost_solvent',
                    'Cost_total',
                    'Data_date_year',
                    'Data_date_month',
                    'Data_date_day',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo'
                    )

        Labels = { 
                    'Machine_drive_history':'稼働履歴',
                    'Cost_electric':'電力費用',
                    'Cost_steam':'蒸気費用',
                    'Cost_gas':'ガス費用',
                    'Cost_water':'水費用',
                    'Cost_solvent':'溶剤費用',
                    'Cost_total':'合計費用',
                    'Data_date_year':'年',
                    'Data_date_month':'月',
                    'Data_date_day':'日',
                    'Data_datetime':'データ取得日',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ'
                    }

