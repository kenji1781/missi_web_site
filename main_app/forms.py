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
                









