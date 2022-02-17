from django import forms
from django.forms import fields, models,widgets

from .models import Customer_Infomation,Equipment_Category,Machine_Model,Trouble_Contents,\
    Unit_Price_Electric,Unit_Price_Steam,Unit_Price_Gas,Unit_Price_Water,Solvent_Name,Solvent_Manufacturer,\
        Solvent0_Conf,Solvent1_Conf,Solvent2_Conf,Solvent3_Conf,Solvent4_Conf,Solvent5_Conf,Solvent6_Conf,Solvent7_Conf,Solvent8_Conf,Solvent9_Conf,\
            Customer_Machine,Trouble_History,Customer_Machine_Recipe,Machine_Drive_History,\
                Cost_Electric,Cost_Steam,Cost_Gas,Cost_Water,Cost_Solvent,Cost_Total,Setting_Item,\
                    Mail_Notification,Maintenance_Mail_Setting,Machine_Temperature_Log,Machine_Log,Plc_Output_Count_Log


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
class Solvent0ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent0_Conf
        fields = ('Solvent0_name','Solvent0_manu','Unit_price_solvent0','Solvent0_input_date','Solvent0_memo')
        widgets = {
            'Solvent0_input_date':DateInput(),
        }
        labels = {
                    'Solvent0_name':'溶剤名',
                    'Solvent0_manu':'溶剤メーカー',
                    'Unit_price_solvent0':'単価：（￥）',
                    'Solvent0_input_date':'登録日',
                    'Solvent0_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent0_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent0_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent0'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent0_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent0_memo'].widgets.attrs["class"] = "form-control"


class Solvent0ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent0_Conf
        fields = ('Solvent0_name','Solvent0_manu','Unit_price_solvent0','Solvent0_input_date','Solvent0_memo')
        widgets = {
            'Solvent0_input_date':DateInput(),
        }
        labels = {
                    'Solvent0_name':'溶剤名',
                    'Solvent0_manu':'溶剤メーカー',
                    'Unit_price_solvent0':'単価：（￥）',
                    'Solvent0_input_date':'登録日',
                    'Solvent0_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent0_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent0_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent0'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent0_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent0_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class Solvent1ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent1_Conf
        fields = ('Solvent1_name','Solvent1_manu','Unit_price_solvent1','Solvent1_input_date','Solvent1_memo')
        widgets = {
            'Solvent1_input_date':DateInput(),
        }
        labels = {
                    'Solvent1_name':'溶剤名',
                    'Solvent1_manu':'溶剤メーカー',
                    'Unit_price_solvent1':'単価：（￥）',
                    'Solvent1_input_date':'登録日',
                    'Solvent1_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent1_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent1_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent1'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent1_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent1_memo'].widgets.attrs["class"] = "form-control"


class Solvent1ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent1_Conf
        fields = ('Solvent1_name','Solvent1_manu','Unit_price_solvent1','Solvent1_input_date','Solvent1_memo')
        widgets = {
            'Solvent1_input_date':DateInput(),
        }
        labels = {
                    'Solvent1_name':'溶剤名',
                    'Solvent1_manu':'溶剤メーカー',
                    'Unit_price_solvent1':'単価：（￥）',
                    'Solvent1_input_date':'登録日',
                    'Solvent1_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent1_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent1_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent1'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent1_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent1_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class Solvent2ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent2_Conf
        fields = ('Solvent2_name','Solvent2_manu','Unit_price_solvent2','Solvent2_input_date','Solvent2_memo')
        widgets = {
            'Solvent2_input_date':DateInput(),
        }
        labels = {
                    'Solvent2_name':'溶剤名',
                    'Solvent2_manu':'溶剤メーカー',
                    'Unit_price_solvent2':'単価：（￥）',
                    'Solvent2_input_date':'登録日',
                    'Solvent2_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent2_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent2_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent2'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent2_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent2_memo'].widgets.attrs["class"] = "form-control"


class Solvent2ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent2_Conf
        fields = ('Solvent2_name','Solvent2_manu','Unit_price_solvent2','Solvent2_input_date','Solvent2_memo')
        widgets = {
            'Solvent2_input_date':DateInput(),
        }
        labels = {
                    'Solvent2_name':'溶剤名',
                    'Solvent2_manu':'溶剤メーカー',
                    'Unit_price_solvent2':'単価：（￥）',
                    'Solvent2_input_date':'登録日',
                    'Solvent2_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent2_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent2_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent2'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent2_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent2_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class Solvent3ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent3_Conf
        fields = ('Solvent3_name','Solvent3_manu','Unit_price_solvent3','Solvent3_input_date','Solvent3_memo')
        widgets = {
            'Solvent3_input_date':DateInput(),
        }
        labels = {
                    'Solvent3_name':'溶剤名',
                    'Solvent3_manu':'溶剤メーカー',
                    'Unit_price_solvent3':'単価：（￥）',
                    'Solvent3_input_date':'登録日',
                    'Solvent3_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent3_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent3_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent3'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent3_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent3_memo'].widgets.attrs["class"] = "form-control"


class Solvent3ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent3_Conf
        fields = ('Solvent3_name','Solvent3_manu','Unit_price_solvent3','Solvent3_input_date','Solvent3_memo')
        widgets = {
            'Solvent3_input_date':DateInput(),
        }
        labels = {
                    'Solvent3_name':'溶剤名',
                    'Solvent3_manu':'溶剤メーカー',
                    'Unit_price_solvent3':'単価：（￥）',
                    'Solvent3_input_date':'登録日',
                    'Solvent3_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent3_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent3_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent3'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent3_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent3_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class Solvent4ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent4_Conf
        fields = ('Solvent4_name','Solvent4_manu','Unit_price_solvent4','Solvent4_input_date','Solvent4_memo')
        widgets = {
            'Solvent4_input_date':DateInput(),
        }
        labels = {
                    'Solvent4_name':'溶剤名',
                    'Solvent4_manu':'溶剤メーカー',
                    'Unit_price_solvent4':'単価：（￥）',
                    'Solvent4_input_date':'登録日',
                    'Solvent4_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent4_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent4_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent4'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent4_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent4_memo'].widgets.attrs["class"] = "form-control"


class Solvent4ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent4_Conf
        fields = ('Solvent4_name','Solvent4_manu','Unit_price_solvent4','Solvent4_input_date','Solvent4_memo')
        widgets = {
            'Solvent4_input_date':DateInput(),
        }
        labels = {
                    'Solvent4_name':'溶剤名',
                    'Solvent4_manu':'溶剤メーカー',
                    'Unit_price_solvent4':'単価：（￥）',
                    'Solvent4_input_date':'登録日',
                    'Solvent4_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent4_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent4_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent4'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent4_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent4_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class Solvent5ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent5_Conf
        fields = ('Solvent5_name','Solvent5_manu','Unit_price_solvent5','Solvent5_input_date','Solvent5_memo')
        widgets = {
            'Solvent5_input_date':DateInput(),
        }
        labels = {
                    'Solvent5_name':'溶剤名',
                    'Solvent5_manu':'溶剤メーカー',
                    'Unit_price_solvent5':'単価：（￥）',
                    'Solvent5_input_date':'登録日',
                    'Solvent5_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent5_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent5_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent5'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent5_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent5_memo'].widgets.attrs["class"] = "form-control"


class Solvent5ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent5_Conf
        fields = ('Solvent5_name','Solvent5_manu','Unit_price_solvent5','Solvent5_input_date','Solvent5_memo')
        widgets = {
            'Solvent5_input_date':DateInput(),
        }
        labels = {
                    'Solvent5_name':'溶剤名',
                    'Solvent5_manu':'溶剤メーカー',
                    'Unit_price_solvent5':'単価：（￥）',
                    'Solvent5_input_date':'登録日',
                    'Solvent5_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent5_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent5_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent5'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent5_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent5_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class Solvent6ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent6_Conf
        fields = ('Solvent6_name','Solvent6_manu','Unit_price_solvent6','Solvent6_input_date','Solvent6_memo')
        widgets = {
            'Solvent6_input_date':DateInput(),
        }
        labels = {
                    'Solvent6_name':'溶剤名',
                    'Solvent6_manu':'溶剤メーカー',
                    'Unit_price_solvent6':'単価：（￥）',
                    'Solvent6_input_date':'登録日',
                    'Solvent6_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent6_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent6_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent6'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent6_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent6_memo'].widgets.attrs["class"] = "form-control"


class Solvent6ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent6_Conf
        fields = ('Solvent6_name','Solvent6_manu','Unit_price_solvent6','Solvent6_input_date','Solvent6_memo')
        widgets = {
            'Solvent6_input_date':DateInput(),
        }
        labels = {
                    'Solvent6_name':'溶剤名',
                    'Solvent6_manu':'溶剤メーカー',
                    'Unit_price_solvent6':'単価：（￥）',
                    'Solvent6_input_date':'登録日',
                    'Solvent6_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent6_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent6_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent6'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent6_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent6_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class Solvent7ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent7_Conf
        fields = ('Solvent7_name','Solvent7_manu','Unit_price_solvent7','Solvent7_input_date','Solvent7_memo')
        widgets = {
            'Solvent7_input_date':DateInput(),
        }
        labels = {
                    'Solvent7_name':'溶剤名',
                    'Solvent7_manu':'溶剤メーカー',
                    'Unit_price_solvent7':'単価：（￥）',
                    'Solvent7_input_date':'登録日',
                    'Solvent7_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent7_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent7_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent7'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent7_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent7_memo'].widgets.attrs["class"] = "form-control"


class Solvent7ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent7_Conf
        fields = ('Solvent7_name','Solvent7_manu','Unit_price_solvent7','Solvent7_input_date','Solvent7_memo')
        widgets = {
            'Solvent7_input_date':DateInput(),
        }
        labels = {
                    'Solvent7_name':'溶剤名',
                    'Solvent7_manu':'溶剤メーカー',
                    'Unit_price_solvent7':'単価：（￥）',
                    'Solvent7_input_date':'登録日',
                    'Solvent7_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent7_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent7_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent7'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent7_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent7_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################
class Solvent8ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent8_Conf
        fields = ('Solvent8_name','Solvent8_manu','Unit_price_solvent8','Solvent8_input_date','Solvent8_memo')
        widgets = {
            'Solvent8_input_date':DateInput(),
        }
        labels = {
                    'Solvent8_name':'溶剤名',
                    'Solvent8_manu':'溶剤メーカー',
                    'Unit_price_solvent8':'単価：（￥）',
                    'Solvent8_input_date':'登録日',
                    'Solvent8_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent8_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent8_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent8'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent8_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent8_memo'].widgets.attrs["class"] = "form-control"


class Solvent8ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent8_Conf
        fields = ('Solvent8_name','Solvent8_manu','Unit_price_solvent8','Solvent8_input_date','Solvent8_memo')
        widgets = {
            'Solvent8_input_date':DateInput(),
        }
        labels = {
                    'Solvent8_name':'溶剤名',
                    'Solvent8_manu':'溶剤メーカー',
                    'Unit_price_solvent8':'単価：（￥）',
                    'Solvent8_input_date':'登録日',
                    'Solvent8_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent8_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent8_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent8'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent8_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent8_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################
class Solvent9ConfCreateForm(forms.ModelForm):
    class Meta:
        model = Solvent9_Conf
        fields = ('Solvent9_name','Solvent9_manu','Unit_price_solvent9','Solvent9_input_date','Solvent9_memo')
        widgets = {
            'Solvent9_input_date':DateInput(),
        }
        labels = {
                    'Solvent9_name':'溶剤名',
                    'Solvent9_manu':'溶剤メーカー',
                    'Unit_price_solvent9':'単価：（￥）',
                    'Solvent9_input_date':'登録日',
                    'Solvent9_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent9_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent9_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent9'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent9_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent9_memo'].widgets.attrs["class"] = "form-control"


class Solvent9ConfUpdateForm(forms.ModelForm):
    class Meta:
        model = Solvent9_Conf
        fields = ('Solvent9_name','Solvent9_manu','Unit_price_solvent9','Solvent9_input_date','Solvent9_memo')
        widgets = {
            'Solvent9_input_date':DateInput(),
        }
        labels = {
                    'Solvent9_name':'溶剤名',
                    'Solvent9_manu':'溶剤メーカー',
                    'Unit_price_solvent9':'単価：（￥）',
                    'Solvent9_input_date':'登録日',
                    'Solvent9_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Solvent9_name'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent9_manu'].widgets.attrs["class"] = "form-control"
                self.fields['Unit_price_solvent9'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent9_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Solvent9_memo'].widgets.attrs["class"] = "form-control"

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
        fields = ('Trouble_contents','Trouble_occurrence_time','Trouble_recovery_time')
        labels = {
                    'Trouble_contents':'異常項目',
                    'Trouble_occurrence_time':'発生時刻',
                    'Trouble_recovery_time':'復帰時刻',
                    
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Trouble_contents'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_occurrence_time'].widgets.attrs["class"] = "form-control"
                self.fields['Trouble_recovery_time'].widgets.attrs["class"] = "form-control"
                               
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
        fields = ('Trouble_contents','Trouble_occurrence_time','Trouble_recovery_time')
        labels = {
                    'Trouble_contents':'異常項目',
                    'Trouble_occurrence_time':'発生時刻',
                    'Trouble_recovery_time':'復帰時刻',
                                        
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
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
                    'Setting_item_id':'品種名ID',
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
                    #'His_id',
                    'Customer_recipe_no',
                    'Machine_model',
                    'Setting_item',
                    
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
                    #'His_id':'履歴ID',
                    'Customer_recipe_no':'コースNo',
                    'Machine_model':'装置',
                    'Setting_item':'品種名',
                    
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
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item'].widgets.attrs["class"] = "form-control"
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
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Setting_item'].widgets.attrs["class"] = "form-control"
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


######################################################################################################

Machine_drive_history_fields = (
                    'Customer_machine_recipe',
                    'Machine_electric_used',
                    'Machine_steam_used',
                    'Machine_gas_used',
                    'Machine_water_used',
                    'Machine_solvent0_used',
                    'Machine_solvent1_used',
                    'Machine_solvent2_used',
                    'Machine_solvent3_used',
                    'Machine_solvent4_used',
                    'Machine_solvent5_used',
                    'Machine_solvent6_used',
                    'Machine_solvent7_used',
                    'Machine_solvent8_used',
                    'Machine_solvent9_used',
                    #'Data_date',
                    #'Data_time',
                    'Data_datetime',
                    'Machine_history_input_date',
                    'Machine_history_memo')

Machine_drive_history_labels = {
                    'Customer_machine_recipe':'装置:コースNo.',
                    'Machine_electric_used':'電力使用量',
                    'Machine_steam_used':'蒸気使用量',
                    'Machine_gas_used':'ガス使用量',
                    'Machine_water_used':'水使用量',
                    'Machine_solvent0_used':'溶剤0使用量',
                    'Machine_solvent1_used':'溶剤1使用量',
                    'Machine_solvent2_used':'溶剤2使用量',
                    'Machine_solvent3_used':'溶剤3使用量',
                    'Machine_solvent4_used':'溶剤4使用量',
                    'Machine_solvent5_used':'溶剤5使用量',
                    'Machine_solvent6_used':'溶剤6使用量',
                    'Machine_solvent7_used':'溶剤7使用量',
                    'Machine_solvent8_used':'溶剤8使用量',
                    'Machine_solvent9_used':'溶剤9使用量',
                    #'Data_date':'データ取得日',
                    #'Data_time':'データ取得時刻',
                    'Data_datetime':'データ取得時刻',
                    'Machine_history_input_date':'登録日',
                    'Machine_history_memo':'メモ',
                }


class MachineDriveHistoryCreateForm(forms.ModelForm):
    class Meta:
        model = Machine_Drive_History
        widgets = {
            'Machine_history_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Machine_drive_history_fields
        labels = Machine_drive_history_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_recipe'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_electric_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_steam_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_gas_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_water_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent0_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent1_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent2_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent3_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent4_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent5_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent6_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent7_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent8_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent9_used'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_history_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_history_memo'].widgets.attrs["class"] = "form-control"
                        

 
class MachineDriveHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Machine_Drive_History
        widgets = {
            'Machine_history_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Machine_drive_history_fields
        labels = Machine_drive_history_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_recipe'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_electric_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_steam_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_gas_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_water_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent0_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent1_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent2_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent3_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent4_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent5_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent6_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent7_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent8_used'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_solvent9_used'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_history_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_history_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################

class MailNotificationCreateForm(forms.ModelForm):
    class Meta:
        model = Mail_Notification
        #fields = ('Equipment_category')
        fields = ('Mail_name','Mail_department','Mail_address','Mail_input_date','Mail_memo')
        
        widgets = {
            'Mail_input_date':DateInput(),
        }
        labels = {
                    'Mail_name':'氏名',
                    'Mail_department':'所属',
                    'Mail_address':'Emailアドレス',
                    'Mail_input_date':'登録日',
                    'Mail_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Mail_name'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_department'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_address'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_memo'].widgets.attrs["class"] = "form-control"
                

class MailNotificationUpdateForm(forms.ModelForm):
    class Meta:
        model = Mail_Notification
        #fields = ('Equipment_category')
        fields = ('Mail_name','Mail_department','Mail_address','Mail_input_date','Mail_memo')
        
        widgets = {
            'Mail_input_date':DateInput(),
        }
        labels = {
                    'Mail_name':'氏名',
                    'Mail_department':'所属',
                    'Mail_address':'Emailアドレス',
                    'Mail_input_date':'登録日',
                    'Mail_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Mail_name'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_department'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_address'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Mail_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################

class MaintenanceEmailCreateForm(forms.ModelForm):
    class Meta:
        model = Maintenance_Mail_Setting
        #fields = ('Equipment_category')
        fields = ('Maintenance_machine_history','Maintenance_mail_notification','Maintenance_threshold_time','Maintenance_threshold_count','Maintenance_send_setting','Maintenance_input_date','Maintenance_memo')
        
        widgets = {
            'Maintenance_input_date':DateInput(),
        }
        labels = {
                    'Maintenance_machine_history':'装置',
                    'Maintenance_mail_notification':'メール発信者',
                    'Maintenance_threshold_time':'閾値:時間',
                    'Maintenance_threshold_count':'閾値:回数',
                    'Maintenance_send_setting':'送信設定',
                    'Maintenance_input_date':'登録日',
                    'Maintenance_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Maintenance_machine_history'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_mail_notification'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_threshold_time'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_threshold_count'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_send_setting'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_memo'].widgets.attrs["class"] = "form-control"
                

class MaintenanceEmailUpdateForm(forms.ModelForm):
    class Meta:
        model = Maintenance_Mail_Setting
        #fields = ('Equipment_category')
        fields = ('Maintenance_machine_history','Maintenance_mail_notification','Maintenance_threshold_time','Maintenance_threshold_count','Maintenance_send_setting','Maintenance_input_date','Maintenance_memo')
        
        widgets = {
            'Maintenance_input_date':DateInput(),
        }
        labels = {
                    'Maintenance_machine_history':'装置',
                    'Maintenance_mail_notification':'メール発信者',
                    'Maintenance_threshold_time':'閾値:時間',
                    'Maintenance_threshold_count':'閾値:回数',
                    'Maintenance_send_setting':'送信設定',
                    'Maintenance_input_date':'登録日',
                    'Maintenance_memo':'メモ',
                }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Maintenance_machine_history'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_mail_notification'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_threshold_time'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_threshold_count'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_send_setting'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Maintenance_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################

Machine_temperature_log_fields = (
                    'Customer_machine_recipe',
                    'Machine_log_temp0',
                    'Machine_log_temp1',
                    'Machine_log_temp2',
                    'Machine_log_temp3',
                    'Machine_log_temp4',
                    'Machine_log_temp5',
                    'Machine_log_temp6',
                    'Machine_log_temp7',
                    'Machine_log_temp8',
                    'Machine_log_temp9',
                    'Machine_log_temp10',
                    'Machine_log_temp11',
                    #'Data_date',
                    #'Data_time',
                    'Data_datetime',
                    'Machine_temp_log_input_date',
                    'Machine_temp_log_memo')

Machine_temperature_log_labels = {
                    'Customer_machine_recipe':'装置',
                    'Machine_log_temp0':'温度0',
                    'Machine_log_temp1':'温度1',
                    'Machine_log_temp2':'温度2',
                    'Machine_log_temp3':'温度3',
                    'Machine_log_temp4':'温度4',
                    'Machine_log_temp5':'温度5',
                    'Machine_log_temp6':'温度6',
                    'Machine_log_temp7':'温度7',
                    'Machine_log_temp8':'温度8',
                    'Machine_log_temp9':'温度9',
                    'Machine_log_temp10':'温度10',
                    'Machine_log_temp11':'温度11',
                    #'Data_date':'データ取得日',
                    #'Data_time':'データ取得時刻',
                    'Data_datetime':'データ取得時刻',
                    'Machine_temp_log_input_date':'登録日',
                    'Machine_temp_log_memo':'メモ',
                }


class MachineTemperatureLogCreateForm(forms.ModelForm):
    class Meta:
        model = Machine_Temperature_Log
        widgets = {
            'Machine_temp_log_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Machine_temperature_log_fields
        labels = Machine_temperature_log_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_recipe'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp0'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp1'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp2'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp3'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp4'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp5'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp6'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp7'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp8'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp9'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp10'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp11'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_temp_log_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_temp_log_memo'].widgets.attrs["class"] = "form-control"
                        

 
class MachineTemperatureLogUpdateForm(forms.ModelForm):
    class Meta:
        model = Machine_Temperature_Log
        widgets = {
            'Machine_temp_log_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Machine_temperature_log_fields
        labels = Machine_temperature_log_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Customer_machine_recipe'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp0'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp1'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp2'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp3'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp4'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp5'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp6'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp7'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp8'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp9'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp10'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_temp11'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_temp_log_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_temp_log_memo'].widgets.attrs["class"] = "form-control"

######################################################################################################

Machine_log_fields = (
                    'Machine_model',
                    'Machine_log_time0',
                    'Machine_log_time1',
                    'Machine_log_time2',
                    'Machine_log_time3',
                    'Machine_log_time4',
                    'Machine_log_time5',
                    'Machine_log_time6',
                    'Machine_log_time7',
                    'Machine_log_time8',
                    'Machine_log_time9',
                    'Machine_log_count0',
                    'Machine_log_count1',
                    'Machine_log_count2',
                    'Machine_log_count3',
                    'Machine_log_count4',
                    'Machine_log_count5',
                    'Machine_log_count6',
                    'Machine_log_count7',
                    'Machine_log_count8',
                    'Machine_log_count9',
                    #'Data_date',
                    #'Data_time',
                    'Data_datetime',
                    'Machine_log_input_date',
                    'Machine_log_memo')

Machine_log_labels = {
                    'Machine_model':'装置',
                    'Machine_log_time0':'稼働時間0',
                    'Machine_log_time1':'稼働時間1',
                    'Machine_log_time2':'稼働時間2',
                    'Machine_log_time3':'稼働時間3',
                    'Machine_log_time4':'稼働時間4',
                    'Machine_log_time5':'稼働時間5',
                    'Machine_log_time6':'稼働時間6',
                    'Machine_log_time7':'稼働時間7',
                    'Machine_log_time8':'稼働時間8',
                    'Machine_log_time9':'稼働時間9',
                    'Machine_log_count0':'稼働回数0',
                    'Machine_log_count1':'稼働回数1',
                    'Machine_log_count2':'稼働回数2',
                    'Machine_log_count3':'稼働回数3',
                    'Machine_log_count4':'稼働回数4',
                    'Machine_log_count5':'稼働回数5',
                    'Machine_log_count6':'稼働回数6',
                    'Machine_log_count7':'稼働回数7',
                    'Machine_log_count8':'稼働回数8',
                    'Machine_log_count9':'稼働回数9',
                    #'Data_date':'データ取得日',
                    #'Data_time':'データ取得時刻',
                    'Data_datetime':'データ取得時刻',
                    'Machine_log_input_date':'登録日',
                    'Machine_log_memo':'メモ',
                }


class MachineLogCreateForm(forms.ModelForm):
    class Meta:
        model = Machine_Log
        widgets = {
            'Machine_log_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Machine_log_fields
        labels = Machine_log_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time0'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time1'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time2'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time3'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time4'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time5'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time6'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time7'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time8'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time9'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count0'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count1'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count2'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count3'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count4'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count5'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count6'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count7'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count8'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count9'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_memo'].widgets.attrs["class"] = "form-control"
                        

 
class MachineLogUpdateForm(forms.ModelForm):
    class Meta:
        model = Machine_Log
        widgets = {
            'Machine_log_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Machine_log_fields
        labels = Machine_log_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time0'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time1'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time2'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time3'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time4'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time5'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time6'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time7'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time8'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_time9'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count0'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count1'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count2'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count3'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count4'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count5'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count6'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count7'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count8'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_count9'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Machine_log_memo'].widgets.attrs["class"] = "form-control"


######################################################################################################

Plc_output_count_log_fields = (
                    'Machine_model',
                    'Plc_count_log_output0',
                    'Plc_count_log_output1',
                    'Plc_count_log_output2',
                    'Plc_count_log_output3',
                    'Plc_count_log_output4',
                    'Plc_count_log_output5',
                    'Plc_count_log_output6',
                    'Plc_count_log_output7',
                    'Plc_count_log_output8',
                    'Plc_count_log_output9',
                    'Plc_count_log_output10',
                    'Plc_count_log_output11',
                    'Plc_count_log_output12',
                    'Plc_count_log_output13',
                    'Plc_count_log_output14',
                    'Plc_count_log_output15',
                    'Plc_count_log_output16',
                    'Plc_count_log_output17',
                    'Plc_count_log_output18',
                    'Plc_count_log_output19',
                    'Plc_count_log_output20',
                    'Plc_count_log_output21',
                    'Plc_count_log_output22',
                    'Plc_count_log_output23',
                    'Plc_count_log_output24',
                    'Plc_count_log_output25',
                    'Plc_count_log_output26',
                    'Plc_count_log_output27',
                    'Plc_count_log_output28',
                    'Plc_count_log_output29',
                    'Plc_count_log_output30',
                    'Plc_count_log_output31',
                    'Plc_count_log_output32',
                    'Plc_count_log_output33',
                    'Plc_count_log_output34',
                    'Plc_count_log_output35',
                    'Plc_count_log_output36',
                    'Plc_count_log_output37',
                    'Plc_count_log_output38',
                    'Plc_count_log_output39',
                    'Plc_count_log_output40',
                    'Plc_count_log_output41',
                    'Plc_count_log_output42',
                    'Plc_count_log_output43',
                    'Plc_count_log_output44',
                    'Plc_count_log_output45',
                    'Plc_count_log_output46',
                    'Plc_count_log_output47',
                    'Plc_count_log_output48',
                    'Plc_count_log_output49',
                    'Plc_count_log_output50',
                    'Plc_count_log_output51',
                    'Plc_count_log_output52',
                    'Plc_count_log_output53',
                    'Plc_count_log_output54',
                    'Plc_count_log_output55',
                    'Plc_count_log_output56',
                    'Plc_count_log_output57',
                    'Plc_count_log_output58',
                    'Plc_count_log_output59',
                    'Plc_count_log_output60',
                    'Plc_count_log_output61',
                    'Plc_count_log_output62',
                    'Plc_count_log_output63',
                    
                    #'Data_date',
                    #'Data_time',
                    'Data_datetime',
                    'Plc_count_log_input_date',
                    'Plc_count_log_memo')

Plc_output_count_log_labels = {
                    'Machine_model':'装置',
                    'Plc_count_log_output0':'OUT:0',
                    'Plc_count_log_output1':'OUT:1',
                    'Plc_count_log_output2':'OUT:2',
                    'Plc_count_log_output3':'OUT:3',
                    'Plc_count_log_output4':'OUT:4',
                    'Plc_count_log_output5':'OUT:5',
                    'Plc_count_log_output6':'OUT:6',
                    'Plc_count_log_output7':'OUT:7',
                    'Plc_count_log_output8':'OUT:8',
                    'Plc_count_log_output9':'OUT:9',
                    'Plc_count_log_output10':'OUT:10',
                    'Plc_count_log_output11':'OUT:11',
                    'Plc_count_log_output12':'OUT:12',
                    'Plc_count_log_output13':'OUT:13',
                    'Plc_count_log_output14':'OUT:14',
                    'Plc_count_log_output15':'OUT:15',
                    'Plc_count_log_output16':'OUT:16',
                    'Plc_count_log_output17':'OUT:17',
                    'Plc_count_log_output18':'OUT:18',
                    'Plc_count_log_output19':'OUT:19',
                    'Plc_count_log_output20':'OUT:20',
                    'Plc_count_log_output21':'OUT:21',
                    'Plc_count_log_output22':'OUT:22',
                    'Plc_count_log_output23':'OUT:23',
                    'Plc_count_log_output24':'OUT:24',
                    'Plc_count_log_output25':'OUT:25',
                    'Plc_count_log_output26':'OUT:26',
                    'Plc_count_log_output27':'OUT:27',
                    'Plc_count_log_output28':'OUT:28',
                    'Plc_count_log_output29':'OUT:29',
                    'Plc_count_log_output30':'OUT:30',
                    'Plc_count_log_output31':'OUT:31',
                    'Plc_count_log_output32':'OUT:32',
                    'Plc_count_log_output33':'OUT:33',
                    'Plc_count_log_output34':'OUT:34',
                    'Plc_count_log_output35':'OUT:35',
                    'Plc_count_log_output36':'OUT:36',
                    'Plc_count_log_output37':'OUT:37',
                    'Plc_count_log_output38':'OUT:38',
                    'Plc_count_log_output39':'OUT:39',
                    'Plc_count_log_output40':'OUT:40',
                    'Plc_count_log_output41':'OUT:41',
                    'Plc_count_log_output42':'OUT:42',
                    'Plc_count_log_output43':'OUT:43',
                    'Plc_count_log_output44':'OUT:44',
                    'Plc_count_log_output45':'OUT:45',
                    'Plc_count_log_output46':'OUT:46',
                    'Plc_count_log_output47':'OUT:47',
                    'Plc_count_log_output48':'OUT:48',
                    'Plc_count_log_output49':'OUT:49',
                    'Plc_count_log_output50':'OUT:50',
                    'Plc_count_log_output51':'OUT:51',
                    'Plc_count_log_output52':'OUT:52',
                    'Plc_count_log_output53':'OUT:53',
                    'Plc_count_log_output54':'OUT:54',
                    'Plc_count_log_output55':'OUT:55',
                    'Plc_count_log_output56':'OUT:56',
                    'Plc_count_log_output57':'OUT:57',
                    'Plc_count_log_output58':'OUT:58',
                    'Plc_count_log_output59':'OUT:59',
                    'Plc_count_log_output60':'OUT:60',
                    'Plc_count_log_output61':'OUT:61',
                    'Plc_count_log_output62':'OUT:62',
                    'Plc_count_log_output63':'OUT:63',
                    #'Data_date':'データ取得日',
                    #'Data_time':'データ取得時刻',
                    'Data_datetime':'データ取得時刻',
                    'Plc_count_log_input_date':'登録日',
                    'Plc_count_log_memo':'メモ',
                }


class PlcOutputCountLogCreateForm(forms.ModelForm):
    class Meta:
        model = Plc_Output_Count_Log
        widgets = {
            'Plc_count_log_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Plc_output_count_log_fields
        labels = Plc_output_count_log_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output0'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output1'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output2'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output3'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output4'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output5'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output6'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output7'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output8'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output9'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output10'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output11'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output12'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output13'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output14'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output15'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output16'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output17'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output18'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output19'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output20'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output21'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output22'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output23'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output24'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output25'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output26'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output27'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output28'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output29'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output30'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output31'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output32'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output33'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output34'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output35'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output36'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output37'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output38'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output39'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output40'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output41'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output42'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output43'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output44'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output45'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output46'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output47'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output48'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output49'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output50'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output51'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output52'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output53'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output54'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output55'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output56'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output57'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output58'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output59'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output60'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output61'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output62'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output63'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_memo'].widgets.attrs["class"] = "form-control"
                        

 
class PlcOutputCountLogUpdateForm(forms.ModelForm):
    class Meta:
        model = Plc_Output_Count_Log
        widgets = {
            'Plc_count_log_input_date':DateInput(),
        }
        #fields = ('Equipment_category')
        
        fields = Plc_output_count_log_fields
        labels = Plc_output_count_log_labels

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                self.fields['Machine_model'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output0'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output1'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output2'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output3'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output4'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output5'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output6'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output7'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output8'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output9'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output10'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output11'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output12'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output13'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output14'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output15'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output16'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output17'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output18'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output19'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output20'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output21'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output22'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output23'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output24'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output25'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output26'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output27'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output28'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output29'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output30'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output31'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output32'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output33'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output34'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output35'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output36'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output37'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output38'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output39'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output40'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output41'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output42'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output43'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output44'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output45'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output46'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output47'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output48'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output49'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output50'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output51'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output52'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output53'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output54'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output55'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output56'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output57'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output58'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output59'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output60'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output61'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output62'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_output63'].widgets.attrs["class"] = "form-control"
                self.fields['data_datetime'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_input_date'].widgets.attrs["class"] = "form-control"
                self.fields['Plc_count_log_memo'].widgets.attrs["class"] = "form-control"
