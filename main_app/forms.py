from django import forms
from django.forms import fields, models,widgets
from models import Machine_data,Machine_setting,Machine_drive_data



class Machine_data_form(forms.ModelForm):
    class Meta:
        models = Machine_data
        fields = '__all__'
        Labels = {  
                    'machine_name':'機種',
                    'machine_unit_no':'号機',
                    'machine_inst_date':'設置日'
                    }


class Machine_setting_form(forms.ModelForm):
    class Meta:
        models = Machine_setting
        fields = [
                    'set_couse_no'
                    ]
        labels = {
                    'set_couse_no':'コース№'
                    }


class Machine_drive_data_form(forms.ModelForm):
    class Meta:
        models = Machine_drive_data
        fields = [  
                    'machine_drying_time',
                    'machine_drive_count',
                    'machine_drive_time_m',
                    'machine_drive_time_s',
                    'machine_steam_used',
                    'machine_electric_used',
                    'machine_air_used',
                    'machine_gas_used',
                    'data_date_year',
                    'data_date_month',
                    'data_date_day'
                    ]
        labels = {  
                    'machine_drying_time':'乾燥時間',
                    'machine_drive_count':'稼働回数',
                    'machine_drive_time_m':'分',
                    'machine_drive_time_s':'秒',
                    'machine_steam_used':'蒸気使用量',
                    'machine_electric_used':'電力使用量',
                    'machine_air_used':'エア使用量',
                    'machine_gas_used':'ガス使用量',
                    'data_date_year':'年',
                    'data_date_month':'月',
                    'data_date_day':'日'
                    }            

