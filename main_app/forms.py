from django import forms
from django.forms import fields, models,widgets

from .models import Customer_Infomation,Equipment_Category,Machine_Model,Trouble_Contents,\
    Unit_Price_Electric,Unit_Price_Steam,Unit_Price_Gas,Unit_Price_Water,Solvent_Name,Solvent_Manufacturer,Solvent_Conf,\
        Customer_Machine,Trouble_History,Customer_Machine_Recipe,Machine_Drive_History,\
            Cost_Electric,Cost_Steam,Cost_Gas,Cost_Water,Cost_Solvent,Cost_Total,Setting_Item


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

######################################################################################################
class WaterPriceCreateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Water
        fields = ('Unit_price_water','Unit_price_water_input_date','Unit_price_water_memo')
        widgets = {
            'Unit_price_water_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_water':'単価：（￥）',
                    'Unit_price_water_input_date':'登録日',
                    'Unit_price_water_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_water'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_water_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_water_memo'].widgets.attrs["class"] = "form-control"


class WaterPriceUpdateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Water
        fields = ('Unit_price_water','Unit_price_water_input_date','Unit_price_water_memo')
        widgets = {
            'Unit_price_water_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_water':'単価：（￥）',
                    'Unit_price_water_input_date':'登録日',
                    'Unit_price_water_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_water'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_water_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_water_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class SteamPriceCreateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Steam
        fields = ('Unit_price_steam','Unit_price_steam_input_date','Unit_price_steam_memo')
        widgets = {
            'Unit_price_steam_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_steam':'単価：（￥）',
                    'Unit_price_steam_input_date':'登録日',
                    'Unit_price_steam_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_steam'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_steam_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_steam_memo'].widgets.attrs["class"] = "form-control"


class SteamPriceUpdateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Steam
        fields = ('Unit_price_steam','Unit_price_steam_input_date','Unit_price_steam_memo')
        widgets = {
            'Unit_price_steam_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_steam':'単価：（￥）',
                    'Unit_price_steam_input_date':'登録日',
                    'Unit_price_steam_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_steam'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_steam_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_steam_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class GasPriceCreateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Gas
        fields = ('Unit_price_gas','Unit_price_gas_input_date','Unit_price_gas_memo')
        widgets = {
            'Unit_price_gas_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_gas':'単価：（￥）',
                    'Unit_price_gas_input_date':'登録日',
                    'Unit_price_gas_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_gas'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_gas_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"

class GasPriceUpdateForm(forms.ModelForm):
    class Meta:
        model = Unit_Price_Gas
        fields = ('Unit_price_gas','Unit_price_gas_input_date','Unit_price_gas_memo')
        widgets = {
            'Unit_price_gas_input_date':DateInput(),
        }
        labels = {
                    'Unit_price_gas':'単価：（￥）',
                    'Unit_price_gas_input_date':'登録日',
                    'Unit_price_gas_memo':'メモ',
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Unit_price_gas'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_gas_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class SolventNameCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent_Name
        fields = ('Solvent_name','Solvent_name_input_date')
        widgets = {
            'Solvent_name_input_date':DateInput(),
        }
        labels = {
                    'Solvent_name':'溶剤名',
                    'Solvent_name_input_date':'登録日',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_name_input_date'].widgets.attrs["class"] = "form-control"
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class SolventNameUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent_Name
        fields = ('Solvent_name','Solvent_name_input_date')
        widgets = {
            'Solvent_name_input_date':DateInput(),
        }
        labels = {
                    'Solvent_name':'溶剤名',
                    'Solvent_name_input_date':'登録日',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_name_input_date'].widgets.attrs["class"] = "form-control"
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"
                
######################################################################################################
class SolventManufacturerCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent_Manufacturer
        fields = ('Solvent_manu','Solvent_manu_input_date')
        widgets = {
            'Solvent_manu_input_date':DateInput(),
        }
        labels = {
                    'Solvent_manu':'溶剤メーカー',
                    'Solvent_manu_input_date':'登録日',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_manu_input_date'].widgets.attrs["class"] = "form-control"
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class SolventManufacturerUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent_Manufacturer
        fields = ('Solvent_manu','Solvent_manu_input_date')
        widgets = {
            'Solvent_manu_input_date':DateInput(),
        }
        labels = {
                    'Solvent_manu':'溶剤メーカー',
                    'Solvent_manu_input_date':'登録日',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_manu_input_date'].widgets.attrs["class"] = "form-control"
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"
                
######################################################################################################
class SolventConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent_Conf
        fields = ('Solvent_name','Solvent_manu','Solvent_unit_price','Solvent_input_date','Solvent_memo')
        widgets = {
            'Solvent_input_date':DateInput(),
        }
        labels = {
                    'Solvent_name':'溶剤名',
                    'Solvent_manu':'溶剤メーカー',
                    'Solvent_unit_price':'単価：（￥）',
                    'Solvent_input_date':'登録日',
                    'Solvent_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_unit_price'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_memo'].widgets.attrs["class"] = "form-control"


class SolventConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent_Conf
        fields = ('Solvent_name','Solvent_manu','Solvent_unit_price','Solvent_input_date','Solvent_memo')
        widgets = {
            'Solvent_input_date':DateInput(),
        }
        labels = {
                    'Solvent_name':'溶剤名',
                    'Solvent_manu':'溶剤メーカー',
                    'Solvent_unit_price':'単価：（￥）',
                    'Solvent_input_date':'登録日',
                    'Solvent_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_unit_price'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class EquipmentCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment_Category
        #fields = ('Equipment_category')
        fields = ('Equipment_category','Equipment_category_input_date')
        
        widgets = {
            'Equipment_category_input_date':DateInput(),
        }
        labels = {
                    'Equipment_category':'装置カテゴリー',
                    'Equipment_category_input_date':'登録日',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Equipment_category'].widgets.attrs["class"] = "form-control"
                self.fields['Equipment_category_input_date'].widgets.attrs["class"] = "form-control"
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class EquipmentCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Equipment_Category
        #fields = ('Equipment_category')
        fields = ('Equipment_category','Equipment_category_input_date')
        
        widgets = {
            'Equipment_category_input_date':DateInput(),
        }
        labels = {
                    'Equipment_category':'装置カテゴリー',
                    'Equipment_category_input_date':'登録日',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Equipment_category'].widgets.attrs["class"] = "form-control"
                self.fields['Equipment_category_input_date'].widgets.attrs["class"] = "form-control"
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"
                

######################################################################################################
class MachineModelCreateForm(forms.ModelForm):
    class Meta:
        model = Machine_Model
        #fields = ('Equipment_category')
        fields = ('Machine_category','Machine_model','Machine_model_input_date','Machine_model_memo')
        
        widgets = {
            'Machine_model_input_date':DateInput(),
        }
        labels = {
                    'Machine_category':'装置カテゴリー',
                    'Machine_model':'装置型式',
                    'Machine_model_input_date':'登録日',
                    'Machine_model_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_category'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class MachineModelUpdateForm(forms.ModelForm):
    class Meta:
        model = Machine_Model
        #fields = ('Equipment_category')
        fields = ('Machine_category','Machine_model','Machine_model_input_date','Machine_model_memo')
        
        widgets = {
            'Machine_model_input_date':DateInput(),
        }
        labels = {
                    'Machine_category':'装置カテゴリー',
                    'Machine_model':'装置型式',
                    'Machine_model_input_date':'登録日',
                    'Machine_model_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_category'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model_memo'].widgets.attrs["class"] = "form-control"
                

######################################################################################################
class CustomerMachineCreateForm(forms.ModelForm):
    class Meta:
        model = Customer_Machine
        #fields = ('Equipment_category')
        fields = ('Customer_machine_id','Machine_model','Customer_machine_unit_no','Customer_machine_inst_date','Customer_machine_input_date','Customer_machine_memo')
        
        widgets = {
            'Customer_machine_inst_date':DateInput(),
            'Customer_machine_input_date':DateInput(),
                }
        labels = {
                    'Customer_machine_id':'装置ID',
                    'Machine_model':'装置型式',
                    'Customer_machine_unit_no':'号機',
                    'Customer_machine_inst_date':'納入日',
                    'Customer_machine_input_date':'登録日',
                    'Customer_machine_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_id'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_unit_no'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_inst_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class CustomerMachineUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer_Machine
        #fields = ('Equipment_category')
        fields = ('Customer_machine_id','Machine_model','Customer_machine_unit_no','Customer_machine_inst_date','Customer_machine_input_date','Customer_machine_memo')
        
        widgets = {
            'Customer_machine_inst_date':DateInput(),
            'Customer_machine_input_date':DateInput(),
                }
        labels = {
                    'Customer_machine_id':'装置ID',
                    'Machine_model':'装置型式',
                    'Customer_machine_unit_no':'号機',
                    'Customer_machine_inst_date':'納入日',
                    'Customer_machine_input_date':'登録日',
                    'Customer_machine_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_id'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_unit_no'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_inst_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class CustomerInfomationCreateForm(forms.ModelForm):
    class Meta:
        model = Customer_Infomation
        #fields = ('Equipment_category')
        fields = ('Customer_name','Customer_tel_number','Customer_pastal_code','Customer_address1','Customer_address2','Customer_address3','Customer_input_date','Customer_memo')
        
        widgets = {
            'Customer_input_date':DateInput(),
                }
        labels = {
                    'Customer_name':'企業名',
                    'Customer_tel_number':'Tel',
                    'Customer_pastal_code':'〒',
                    'Customer_address1':'住所１',
                    'Customer_address2':'住所２',
                    'Customer_address3':'住所３',
                    'Customer_input_date':'登録日',
                    'Customer_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_name'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_tel_number'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_pastal_code'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_address1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_address2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_address3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class CustomerInfomationUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer_Infomation
        #fields = ('Equipment_category')
        fields = ('Customer_name','Customer_tel_number','Customer_pastal_code','Customer_address1','Customer_address2','Customer_address3','Customer_input_date','Customer_memo')
        
        widgets = {
            'Customer_input_date':DateInput(),
                }
        labels = {
                    'Customer_name':'企業名',
                    'Customer_tel_number':'Tel',
                    'Customer_pastal_code':'〒',
                    'Customer_address1':'住所１',
                    'Customer_address2':'住所２',
                    'Customer_address3':'住所３',
                    'Customer_input_date':'登録日',
                    'Customer_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_name'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_tel_number'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_pastal_code'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_address1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_address2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_address3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class TroubleContentsCreateForm(forms.ModelForm):
    class Meta:
        model = Trouble_Contents
        #fields = ('Equipment_category')
        fields = ('Machine_model','Trouble_no','Trouble_contents','Trouble_input_date','Trouble_memo')
        
        widgets = {
            'Trouble_input_date':DateInput(),
        }
        labels = {
                    'Machine_model':'装置型式',
                    'Trouble_no':'異常No.',
                    'Trouble_contents':'異常項目',
                    'Trouble_input_date':'登録日',
                    'Trouble_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_no'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_contents'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class TroubleContentsUpdateForm(forms.ModelForm):
    class Meta:
        model = Trouble_Contents
        #fields = ('Equipment_category')
        fields = ('Machine_model','Trouble_no','Trouble_contents','Trouble_input_date','Trouble_memo')
        
        widgets = {
            'Trouble_input_date':DateInput(),
        }
        labels = {
                    'Machine_model':'装置型式',
                    'Trouble_no':'異常No.',
                    'Trouble_contents':'異常',
                    'Trouble_input_date':'登録日',
                    'Trouble_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_no'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_contents'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_memo'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class TroubleHistoryCreateForm(forms.ModelForm):
    Trouble_occurrence_time = forms.SplitDateTimeField(label='発生時刻')
    Trouble_recovery_time = forms.SplitDateTimeField(label='復帰時刻')
    class Meta:
        model = Trouble_History
        widgets = {
            'Trouble_input_date_0':DateInput(),
        }
        #fields = ('Equipment_category')
        fields = ('Customer_machine_id','Machine_model','Trouble_no','Trouble_contents','Trouble_occurrence_time','Trouble_recovery_time')
        labels = {
                    'Customer_machine_id':'装置ID',
                    'Machine_model':'装置型式',
                    'Trouble_no':'異常No.',
                    'Trouble_contents':'異常項目',
                    'Trouble_occurrence_time':'発生時刻',
                    'Trouble_recovery_time':'復帰時刻',
                    
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_id'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_no'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_contents'].widgets.attrs["class"] = "form-control"
                                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class TroubleHistoryUpdateForm(forms.ModelForm):
    Trouble_occurrence_time = forms.SplitDateTimeField(label='発生時刻')
    Trouble_recovery_time = forms.SplitDateTimeField(label='復帰時刻')
    class Meta:
        model = Trouble_History
        """
        dateTimeOptions = {
            'format':'yyyy-mm-dd HH:II:ss'
        }
        widgets = {
            'Trouble_occurrence_time':datetimewidget(options=dateTimeOptions),
            'Trouble_recovery_time':datetimewidget(options=dateTimeOptions),
        }
        """        
        fields = ('Customer_machine_id','Machine_model','Trouble_no','Trouble_contents','Trouble_occurrence_time','Trouble_recovery_time')
        labels = {
                    'Customer_machine_id':'装置ID',
                    'Machine_model':'装置型式',
                    'Trouble_no':'異常No.',
                    'Trouble_contents':'異常項目',
                                        
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_id'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_no'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_contents'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_occurrence_time'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_recovery_time'].widgets.attrs["class"] = "form-control"
                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class SettingItemCreateForm(forms.ModelForm):
    class Meta:
        model = Setting_Item
        widgets = {
            'Setting_item_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        fields = ('Setting_item_id','Setting_item_name','Setting_item_input_date','Setting_item_memo')
        labels = {
                    'Setting_item_id':'品種ID',
                    'Setting_item_name':'品種名',
                    'Setting_item_input_date':'登録日',
                    'Setting_item_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Setting_item_id'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item_name'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item_memo'].widgets.attrs["class"] = "form-control"
                                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"


class SettingItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Setting_Item
        widgets = {
            'Setting_item_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        fields = ('Setting_item_id','Setting_item_name','Setting_item_input_date','Setting_item_memo')
        labels = {
                    'Setting_item_id':'品種ID',
                    'Setting_item_name':'品種名',
                    'Setting_item_input_date':'登録日',
                    'Setting_item_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Setting_item_id'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item_name'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item_memo'].widgets.attrs["class"] = "form-control"
                                
                #self.fields['Unit_price_gas_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
Customer__recipe_fields = (
                    'Customer_machine_id',
                    'Machine_model',
                    'Recipe_id',
                    'Recipe_name',
                    'Customer_recipe_no',
                    'Customer_recipe_time0',
                    'Customer_recipe_time1',
                    'Customer_recipe_time2',
                    'Customer_recipe_time3',
                    'Customer_recipe_time4',
                    'Customer_recipe_temp0',
                    'Customer_recipe_temp1',
                    'Customer_recipe_temp2',
                    'Customer_recipe_temp3',
                    'Customer_recipe_temp4',
                    'Customer_recipe_temp5',
                    'Customer_recipe_temp6',
                    'Customer_recipe_temp7',
                    'Customer_recipe_temp8',
                    'Customer_recipe_temp9',
                    'Customer_recipe_temp10',
                    'Customer_recipe_temp11',
                    'Customer_recipe_conf0',
                    'Customer_recipe_conf1',
                    'Customer_recipe_conf2',
                    'Customer_recipe_conf3',
                    'Customer_recipe_conf4',
                    'Customer_recipe_conf5',
                    'Customer_recipe_conf6',
                    'Customer_recipe_conf7',
                    'Customer_recipe_conf8',
                    'Customer_recipe_conf9',
                    'Customer_recipe_conf10',
                    'Customer_recipe_conf11',
                    'Customer_recipe_conf12',
                    'Customer_recipe_conf13',
                    'Customer_recipe_conf14',
                    'Customer_recipe_conf15',
                    'Customer_recipe_conf16',
                    'Customer_recipe_conf17',
                    'Customer_recipe_conf18',
                    'Customer_recipe_conf19',
                    'Customer_recipe_set_value0',
                    'Customer_recipe_set_value1',
                    'Customer_recipe_set_value2',
                    'Customer_recipe_set_value3',
                    'Customer_recipe_set_value4',
                    'Customer_recipe_set_value5',
                    'Customer_recipe_set_value6',
                    'Customer_recipe_set_value7',
                    'Customer_recipe_set_value8',
                    'Customer_recipe_set_value9',
                    'Customer_recipe_set_value10',
                    'Customer_recipe_set_value11',
                    'Customer_recipe_set_value12',
                    'Customer_recipe_set_value13',
                    'Customer_recipe_set_value14',
                    'Customer_recipe_set_value15',
                    'Customer_recipe_set_value16',
                    'Customer_recipe_set_value17',
                    'Customer_recipe_set_value18',
                    'Customer_recipe_set_value19',
                    'Customer_machine_input_date',
                    'Customer_machine_memo')

Customer__recipe_labels = {
                    'Customer_machine_id':'装置ID',
                    'Machine_model':'装置',
                    'Recipe_id':'品種ID',
                    'Recipe_name':'品種名',
                    'Customer_recipe_no':'品種No',
                    'Customer_recipe_time0':'運転時間設定0',
                    'Customer_recipe_time1':'運転時間設定1',
                    'Customer_recipe_time2':'運転時間設定2',
                    'Customer_recipe_time3':'運転時間設定3',
                    'Customer_recipe_time4':'運転時間設定4',
                    'Customer_recipe_temp0':'温度設定0',
                    'Customer_recipe_temp1':'温度設定1',
                    'Customer_recipe_temp2':'温度設定2',
                    'Customer_recipe_temp3':'温度設定3',
                    'Customer_recipe_temp4':'温度設定4',
                    'Customer_recipe_temp5':'温度設定5',
                    'Customer_recipe_temp6':'温度設定6',
                    'Customer_recipe_temp7':'温度設定7',
                    'Customer_recipe_temp8':'温度設定8',
                    'Customer_recipe_temp9':'温度設定9',
                    'Customer_recipe_temp10':'温度設定10',
                    'Customer_recipe_temp11':'温度設定11',
                    'Customer_recipe_conf0':'設定0',
                    'Customer_recipe_conf1':'設定1',
                    'Customer_recipe_conf2':'設定2',
                    'Customer_recipe_conf3':'設定3',
                    'Customer_recipe_conf4':'設定4',
                    'Customer_recipe_conf5':'設定5',
                    'Customer_recipe_conf6':'設定6',
                    'Customer_recipe_conf7':'設定7',
                    'Customer_recipe_conf8':'設定8',
                    'Customer_recipe_conf9':'設定9',
                    'Customer_recipe_conf10':'設定10',
                    'Customer_recipe_conf11':'設定11',
                    'Customer_recipe_conf12':'設定12',
                    'Customer_recipe_conf13':'設定13',
                    'Customer_recipe_conf14':'設定14',
                    'Customer_recipe_conf15':'設定15',
                    'Customer_recipe_conf16':'設定16',
                    'Customer_recipe_conf17':'設定17',
                    'Customer_recipe_conf18':'設定18',
                    'Customer_recipe_conf19':'設定19',
                    'Customer_recipe_set_value0':'設定値0',
                    'Customer_recipe_set_value1':'設定値1',
                    'Customer_recipe_set_value2':'設定値2',
                    'Customer_recipe_set_value3':'設定値3',
                    'Customer_recipe_set_value4':'設定値4',
                    'Customer_recipe_set_value5':'設定値5',
                    'Customer_recipe_set_value6':'設定値6',
                    'Customer_recipe_set_value7':'設定値7',
                    'Customer_recipe_set_value8':'設定値8',
                    'Customer_recipe_set_value9':'設定値9',
                    'Customer_recipe_set_value10':'設定値10',
                    'Customer_recipe_set_value11':'設定値11',
                    'Customer_recipe_set_value12':'設定値12',
                    'Customer_recipe_set_value13':'設定値13',
                    'Customer_recipe_set_value14':'設定値14',
                    'Customer_recipe_set_value15':'設定値15',
                    'Customer_recipe_set_value16':'設定値16',
                    'Customer_recipe_set_value17':'設定値17',
                    'Customer_recipe_set_value18':'設定値18',
                    'Customer_recipe_set_value19':'設定値19',
                    'Customer_machine_input_date':'登録日',
                    'Customer_machine_memo':'メモ',
                }


class CustomerMachineRecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Customer_Machine_Recipe
        widgets = {
            'Customer_machine_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Customer__recipe_fields
        labels = Customer__recipe_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_id'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Recipe_id'].widgets.attrs["class"] = "form-control"
                self.fields['Recipe_name'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_no'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp5'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp6'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp7'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp8'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp9'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp10'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp11'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf5'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf6'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf7'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf8'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf9'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf10'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf11'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf12'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf13'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf14'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf15'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf16'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf17'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf18'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf19'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value5'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value6'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value7'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value8'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value9'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value10'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value11'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value12'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value13'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value14'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value15'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value16'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value17'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value18'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value19'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_memo'].widgets.attrs["class"] = "form-control"
        

 
class CustomerMachineRecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer_Machine_Recipe
        widgets = {
            'Customer_machine_input_date':DateInput(),
        }
        
        fields = Customer__recipe_fields
        labels = Customer__recipe_labels
       
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_id'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Recipe_id'].widgets.attrs["class"] = "form-control"
                self.fields['Recipe_name'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_no'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_time4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp5'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp6'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp7'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp8'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp9'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp10'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_temp11'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf5'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf6'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf7'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf8'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf9'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf10'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf11'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf12'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf13'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf14'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf15'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf16'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf17'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf18'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_conf19'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value0'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value1'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value2'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value3'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value4'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value5'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value6'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value7'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value8'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value9'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value10'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value11'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value12'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value13'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value14'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value15'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value16'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value17'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value18'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_recipe_set_value19'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Customer_machine_memo'].widgets.attrs["class"] = "form-control"
