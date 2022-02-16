from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from django.db.models.fields.related import ForeignKey



#メーカー登録情報#####################################################################

# 客先情報☆
class Customer_Infomation(models.Model):
    Customer_name = models.CharField(verbose_name='企業名',max_length=20,blank=False,null=False)
    #tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("半角数字 11桁で入力して下さい。 例:'09012345678'"))
    Customer_tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号',blank=True,null=True)
    
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("半角数字 7桁で入力して下さい。 例:'1234567'"))
    Customer_pastal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号',blank=True,null=True)    
    
    Customer_address1 = models.CharField(verbose_name='都道府県',max_length=40,blank=True,null=True)
    Customer_address2 = models.CharField(verbose_name='市町村番地',max_length=40,blank=True,null=True)
    Customer_address3 = models.CharField(verbose_name='建物名',max_length=40,blank=True,null=True)
    Customer_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Customer_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 企業名 : '+ self.Customer_name + ' TEL : ' + self.Customer_tel_number + \
            ' メモ: ' + self.Customer_memo + ' 登録日: ' +  str(self.Customer_input_date) + '>'
    
    class Meta:
        verbose_name_plural = ('客先情報')


#装置カテゴリー☆
class Equipment_Category(models.Model):
    Equipment_category = CharField(verbose_name='装置カテゴリー',max_length=10,blank=False,null=False,unique=True)
    Equipment_category_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)

    def __str__(self):
       return str(self.Equipment_category)

    class Meta:
        verbose_name_plural = ('装置カテゴリー')


#装置型式☆
class Machine_Model(models.Model):
    Machine_category = models.ForeignKey(Equipment_Category,on_delete=CASCADE,verbose_name='装置カテゴリー')
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=False,null=False,unique=True)
    Machine_model_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_model_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return str(self.Machine_model)

    class Meta:
        verbose_name_plural = ('装置型式')

#客先装置
class Customer_Machine(models.Model):
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=False,null=False,unique=True)
    Machine_model = models.ForeignKey(Machine_Model,on_delete=CASCADE,verbose_name='装置')
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_machine_inst_date = models.DateField(verbose_name='納入日',blank=True,null=True)
    Customer_machine_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Customer_machine_memo = models.TextField(verbose_name='メモ',blank=True,max_length=50)

    def __str__(self):
       return 'ID:' + str(self.Customer_machine_id) + '  ' + str(self.Machine_model) + ': #' +\
            str(self.Customer_machine_unit_no)

    class Meta:
        verbose_name_plural = ('客先装置')


#異常内容
class Trouble_Contents(models.Model):
    Machine_model = models.ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Trouble_no = models.IntegerField(verbose_name='異常No',validators=[MinValueValidator(0)],blank=True,null=True)
    Trouble_contents = models.CharField(verbose_name='異常項目',max_length=20,blank=True,null=True)
    Trouble_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Trouble_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    

    def __str__(self):
       return str(self.Machine_model) + ' '+\
            str(self.Trouble_contents)
    
    class Meta:
        verbose_name_plural = ('異常内容')
        constraints = [
            models.UniqueConstraint(fields=['Machine_model','Trouble_no'],name='unique_trouble_no'),
        ]



class Trouble_History(models.Model):
    Trouble_contents = models.ForeignKey(Trouble_Contents,on_delete=CASCADE,verbose_name='異常')
    Trouble_occurrence_time = models.DateTimeField(verbose_name='発生時刻',blank=True,null=True)   
    Trouble_recovery_time = models.DateTimeField(verbose_name='復帰時刻',blank=True,null=True)
    time_calc = models.IntegerField(verbose_name='ロスタイム計算用',blank=True,null=True)
    Trouble_loss_time = models.CharField(verbose_name='ロスタイム',max_length=20,blank=True,null=True)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)

    def __str__(self):
       return str(self.Trouble_contents)
                
    class Meta:
        verbose_name_plural = ('異常履歴')

#コース名
class Recipe_Name(models.Model):
    Recipe_id = models.IntegerField(verbose_name='品種ID',validators=[MinValueValidator(0)],default=1,blank=True,null=True)
    Racipe_name = models.CharField(verbose_name='品種名',max_length=20,blank=True,null=True)
    Racipe_name_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Racipe_name_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 品種ID : ' + str(self.Recipe_id) + \
            ' 品種名 : ' + str(self.Racipe_name) + \
        '>'

    class Meta:
        verbose_name_plural = ('レシピ情報')
        constraints = [
            models.UniqueConstraint(fields=['Recipe_id','Racipe_name'],name='unique_recipe_name'),
        ]

class Setting_Item(models.Model):
    Setting_item_id = models.IntegerField(verbose_name='品種名ID',validators=[MinValueValidator(0)],blank=True,null=True,unique=True)
    Setting_item_name = models.CharField(verbose_name='品種名',max_length=20,blank=True,null=True,unique=True)
    Setting_item_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Setting_item_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return 'ID:' + str(self.Setting_item_id) + ' ' + str(self.Setting_item_name)

    class Meta:
        verbose_name_plural = ('設定項目')
        

#レシピ
class Customer_Machine_Recipe(models.Model):
    Machine_model = models.ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Setting_item = models.ForeignKey(Setting_Item,on_delete=CASCADE,verbose_name='コース名')
    Customer_recipe_no = models.IntegerField(verbose_name='コースNo',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Customer_recipe_time0 = models.FloatField(verbose_name='運転時間設定0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_time1 = models.FloatField(verbose_name='運転時間設定1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_time2 = models.FloatField(verbose_name='運転時間設定2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_time3 = models.FloatField(verbose_name='運転時間設定3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_time4 = models.FloatField(verbose_name='運転時間設定4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp0 = models.FloatField(verbose_name='温度設定0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp1 = models.FloatField(verbose_name='温度設定1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp2 = models.FloatField(verbose_name='温度設定2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp3 = models.FloatField(verbose_name='温度設定3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp4 = models.FloatField(verbose_name='温度設定4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp5 = models.FloatField(verbose_name='温度設定5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp6 = models.FloatField(verbose_name='温度設定6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp7 = models.FloatField(verbose_name='温度設定7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp8 = models.FloatField(verbose_name='温度設定8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp9 = models.FloatField(verbose_name='温度設定9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp10 = models.FloatField(verbose_name='温度設定10',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_temp11 = models.FloatField(verbose_name='温度設定11',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_setting_item_id0 = models.IntegerField(verbose_name='設定ID0',blank=True,null=True)
    Customer_recipe_setting_item_id1 = models.IntegerField(verbose_name='設定ID1',blank=True,null=True)
    Customer_recipe_setting_item_id2 = models.IntegerField(verbose_name='設定ID2',blank=True,null=True)
    Customer_recipe_setting_item_id3 = models.IntegerField(verbose_name='設定ID3',blank=True,null=True)
    Customer_recipe_setting_item_id4 = models.IntegerField(verbose_name='設定ID4',blank=True,null=True)
    Customer_recipe_setting_item_id5 = models.IntegerField(verbose_name='設定ID5',blank=True,null=True)
    Customer_recipe_setting_item_id6 = models.IntegerField(verbose_name='設定ID6',blank=True,null=True)
    Customer_recipe_setting_item_id7 = models.IntegerField(verbose_name='設定ID7',blank=True,null=True)
    Customer_recipe_setting_item_id8 = models.IntegerField(verbose_name='設定ID8',blank=True,null=True)
    Customer_recipe_setting_item_id9 = models.IntegerField(verbose_name='設定ID9',blank=True,null=True)
    Customer_recipe_setting_item_id10 = models.IntegerField(verbose_name='設定ID10',blank=True,null=True)
    Customer_recipe_setting_item_id11 = models.IntegerField(verbose_name='設定ID11',blank=True,null=True)
    Customer_recipe_setting_item_id12 = models.IntegerField(verbose_name='設定ID12',blank=True,null=True)
    Customer_recipe_setting_item_id13 = models.IntegerField(verbose_name='設定ID13',blank=True,null=True)
    Customer_recipe_setting_item_id14 = models.IntegerField(verbose_name='設定ID14',blank=True,null=True)
    Customer_recipe_setting_item_id15 = models.IntegerField(verbose_name='設定ID15',blank=True,null=True)
    Customer_recipe_setting_item_id16 = models.IntegerField(verbose_name='設定ID16',blank=True,null=True)
    Customer_recipe_setting_item_id17 = models.IntegerField(verbose_name='設定ID17',blank=True,null=True)
    Customer_recipe_setting_item_id18 = models.IntegerField(verbose_name='設定ID18',blank=True,null=True)
    Customer_recipe_setting_item_id19 = models.IntegerField(verbose_name='設定ID19',blank=True,null=True)
    Customer_recipe_conf0 = models.CharField(verbose_name='設定0',max_length=20,blank=True,null=True)
    Customer_recipe_conf1 = models.CharField(verbose_name='設定1',max_length=20,blank=True,null=True)
    Customer_recipe_conf2 = models.CharField(verbose_name='設定2',max_length=20,blank=True,null=True)
    Customer_recipe_conf3 = models.CharField(verbose_name='設定3',max_length=20,blank=True,null=True)
    Customer_recipe_conf4 = models.CharField(verbose_name='設定4',max_length=20,blank=True,null=True)
    Customer_recipe_conf5 = models.CharField(verbose_name='設定5',max_length=20,blank=True,null=True)
    Customer_recipe_conf6 = models.CharField(verbose_name='設定6',max_length=20,blank=True,null=True)
    Customer_recipe_conf7 = models.CharField(verbose_name='設定7',max_length=20,blank=True,null=True)
    Customer_recipe_conf8 = models.CharField(verbose_name='設定8',max_length=20,blank=True,null=True)
    Customer_recipe_conf9 = models.CharField(verbose_name='設定9',max_length=20,blank=True,null=True)
    Customer_recipe_conf10 = models.CharField(verbose_name='設定10',max_length=20,blank=True,null=True)
    Customer_recipe_conf11 = models.CharField(verbose_name='設定11',max_length=20,blank=True,null=True)
    Customer_recipe_conf12 = models.CharField(verbose_name='設定12',max_length=20,blank=True,null=True)
    Customer_recipe_conf13 = models.CharField(verbose_name='設定13',max_length=20,blank=True,null=True)
    Customer_recipe_conf14 = models.CharField(verbose_name='設定14',max_length=20,blank=True,null=True)
    Customer_recipe_conf15 = models.CharField(verbose_name='設定15',max_length=20,blank=True,null=True)
    Customer_recipe_conf16 = models.CharField(verbose_name='設定16',max_length=20,blank=True,null=True)
    Customer_recipe_conf17 = models.CharField(verbose_name='設定17',max_length=20,blank=True,null=True)
    Customer_recipe_conf18 = models.CharField(verbose_name='設定18',max_length=20,blank=True,null=True)
    Customer_recipe_conf19 = models.CharField(verbose_name='設定19',max_length=20,blank=True,null=True)
    Customer_recipe_set_value0 = models.FloatField(verbose_name='設定値0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value1 = models.FloatField(verbose_name='設定値1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value2 = models.FloatField(verbose_name='設定値2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value3 = models.FloatField(verbose_name='設定値3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value4 = models.FloatField(verbose_name='設定値4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value5 = models.FloatField(verbose_name='設定値5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value6 = models.FloatField(verbose_name='設定値6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value7 = models.FloatField(verbose_name='設定値7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value8 = models.FloatField(verbose_name='設定値8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value9 = models.FloatField(verbose_name='設定値9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value10 = models.FloatField(verbose_name='設定値10',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value11 = models.FloatField(verbose_name='設定値11',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value12 = models.FloatField(verbose_name='設定値12',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value13 = models.FloatField(verbose_name='設定値13',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value14 = models.FloatField(verbose_name='設定値14',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value15 = models.FloatField(verbose_name='設定値15',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value16 = models.FloatField(verbose_name='設定値16',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value17 = models.FloatField(verbose_name='設定値17',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value18 = models.FloatField(verbose_name='設定値18',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_recipe_set_value19 = models.FloatField(verbose_name='設定値19',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Customer_machine_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Customer_machine_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)



    def __str__(self):
       return str(self.Machine_model) + '    ' + \
		    str(self.Setting_item) + '    ' + \
                'コースNo.:' + str(self.Customer_recipe_no)

    class Meta:
        verbose_name_plural = ('レシピ情報')

#電気単価
class Unit_Price_Electric(models.Model):
    Unit_price_electric = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
    Unit_price_electric_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Unit_price_electric_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 単価 : ' + str(self.Unit_price_electric) + ' 登録日 : ' + str(self.Unit_price_electric_input_date) + \
            ' メモ : ' + self.Unit_price_electric_memo + '>'

    class Meta:
        verbose_name_plural = ('電力単価')


#蒸気単価
class Unit_Price_Steam(models.Model):
    Unit_price_steam = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
    Unit_price_steam_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Unit_price_steam_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 単価 : ' + str(self.Unit_price_steam) + ' 登録日 : ' + str(self.Unit_price_steam_input_date) + \
            ' メモ : ' + self.Unit_price_steam_memo + '>'

    class Meta:
        verbose_name_plural = ('蒸気単価')


#ガス単価
class Unit_Price_Gas(models.Model):
    Unit_price_gas = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
    Unit_price_gas_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Unit_price_gas_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 単価 : ' + str(self.Unit_price_gas) + ' 登録日 : ' + str(self.Unit_price_gas_input_date) + \
            ' メモ : ' + self.Unit_price_gas_memo + '>'

    class Meta:
        verbose_name_plural = ('ガス単価')


#水単価
class Unit_Price_Water(models.Model):
    Unit_price_water = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
    Unit_price_water_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Unit_price_water_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 単価 : ' + str(self.Unit_price_water) + ' 登録日 : ' + str(self.Unit_price_water_input_date) + \
            ' メモ : ' + self.Unit_price_water_memo + '>'

    class Meta:
        verbose_name_plural = ('水単価')


#溶剤名
class Solvent_Name(models.Model):
    Solvent_name = models.CharField(verbose_name='溶剤名',max_length=20,blank=True,null=True,unique=True)
    Solvent_name_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    
    def __str__(self):
       return str(self.Solvent_name)
    

    class Meta:
        verbose_name_plural = ('溶剤名')




#溶剤メーカー
class Solvent_Manufacturer(models.Model):
    Solvent_manu = models.CharField(verbose_name='メーカー',max_length=20,blank=True,null=True,unique=True)
    Solvent_manu_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)

    def __str__(self):
       return str(self.Solvent_manu)

    class Meta:
        verbose_name_plural = ('溶剤メーカー')


#設定:溶剤0
class Solvent0_Conf(models.Model):
    Solvent0_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent0_name')
    Solvent0_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent0_manu')
    Unit_price_solvent0 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent0_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent0_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent0_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent0) + \
                ' 登録日 : ' + str(self.Solvent0_input_date) + \
                ' メモ : ' + self.Solvent0_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤0設定')

#設定:溶剤1
class Solvent1_Conf(models.Model):
    Solvent1_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent1_name')
    Solvent1_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent1_manu')
    Unit_price_solvent1 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent1_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent1_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent1_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent1) + \
                ' 登録日 : ' + str(self.Solvent1_input_date) + \
                ' メモ : ' + self.Solvent1_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤1設定')

#設定:溶剤2
class Solvent2_Conf(models.Model):
    Solvent2_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent2_name')
    Solvent2_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent2_manu')
    Unit_price_solvent2 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent2_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent2_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent2_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent2) + \
                ' 登録日 : ' + str(self.Solvent2_input_date) + \
                ' メモ : ' + self.Solvent2_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤2設定')

#設定:溶剤3
class Solvent3_Conf(models.Model):
    Solvent3_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent3_name')
    Solvent3_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent3_manu')
    Unit_price_solvent3 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent3_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent3_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent3_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent3) + \
                ' 登録日 : ' + str(self.Solvent3_input_date) + \
                ' メモ : ' + self.Solvent3_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤3設定')

#設定:溶剤4
class Solvent4_Conf(models.Model):
    Solvent4_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent4_name')
    Solvent4_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent4_manu')
    Unit_price_solvent4 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent4_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent4_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent4_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent4) + \
                ' 登録日 : ' + str(self.Solvent4_input_date) + \
                ' メモ : ' + self.Solvent4_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤4設定')

#設定:溶剤5
class Solvent5_Conf(models.Model):
    Solvent5_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent5_name')
    Solvent5_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent5_manu')
    Unit_price_solvent5 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent5_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent5_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent5_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent5) + \
                ' 登録日 : ' + str(self.Solvent5_input_date) + \
                ' メモ : ' + self.Solvent5_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤5設定')

#設定:溶剤6
class Solvent6_Conf(models.Model):
    Solvent6_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent6_name')
    Solvent6_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent6_manu')
    Unit_price_solvent6 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent6_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent6_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent6_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent6) + \
                ' 登録日 : ' + str(self.Solvent6_input_date) + \
                ' メモ : ' + self.Solvent6_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤6設定')

#設定:溶剤7
class Solvent7_Conf(models.Model):
    Solvent7_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent7_name')
    Solvent7_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent7_manu')
    Unit_price_solvent7 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent7_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent7_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent7_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent7) + \
                ' 登録日 : ' + str(self.Solvent7_input_date) + \
                ' メモ : ' + self.Solvent7_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤7設定')

#設定:溶剤8
class Solvent8_Conf(models.Model):
    Solvent8_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent8_name')
    Solvent8_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent8_manu')
    Unit_price_solvent8 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent8_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent8_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent8_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent8) + \
                ' 登録日 : ' + str(self.Solvent8_input_date) + \
                ' メモ : ' + self.Solvent8_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤8設定')

#設定:溶剤9
class Solvent9_Conf(models.Model):
    Solvent9_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent9_name')
    Solvent9_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent9_manu')
    Unit_price_solvent9 = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent9_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent9_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent9_manu) + \
            ' 単価 : ' + str(self.Unit_price_solvent9) + \
                ' 登録日 : ' + str(self.Solvent9_input_date) + \
                ' メモ : ' + self.Solvent9_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤9設定')

#装置稼働履歴
class Machine_Drive_History(models.Model):
    Customer_machine_recipe = models.ForeignKey(Customer_Machine_Recipe,on_delete=CASCADE,verbose_name='コース名')
    Machine_drive_time0 = models.IntegerField(verbose_name='運転時間0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_time1 = models.IntegerField(verbose_name='運転時間1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_time2 = models.IntegerField(verbose_name='運転時間2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_time3 = models.IntegerField(verbose_name='運転時間3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_time4 = models.IntegerField(verbose_name='運転時間4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp0 = models.IntegerField(verbose_name='温度0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp1 = models.IntegerField(verbose_name='温度1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp2 = models.IntegerField(verbose_name='温度2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp3 = models.IntegerField(verbose_name='温度3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp4 = models.IntegerField(verbose_name='温度4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp5 = models.IntegerField(verbose_name='温度5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp6 = models.IntegerField(verbose_name='温度6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp7 = models.IntegerField(verbose_name='温度7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp8 = models.IntegerField(verbose_name='温度8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp9 = models.IntegerField(verbose_name='温度9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp10 = models.IntegerField(verbose_name='温度10',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_temp11 = models.IntegerField(verbose_name='温度11',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_count = models.IntegerField(verbose_name='稼働回数',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent0_used = models.FloatField(verbose_name='溶剤0使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent1_used = models.FloatField(verbose_name='溶剤1使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent2_used = models.FloatField(verbose_name='溶剤2使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent3_used = models.FloatField(verbose_name='溶剤3使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent4_used = models.FloatField(verbose_name='溶剤4使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent5_used = models.FloatField(verbose_name='溶剤5使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent6_used = models.FloatField(verbose_name='溶剤6使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent7_used = models.FloatField(verbose_name='溶剤7使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent8_used = models.FloatField(verbose_name='溶剤8使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_solvent9_used = models.FloatField(verbose_name='溶剤9使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_electric = models.FloatField(verbose_name='電力単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_steam = models.FloatField(verbose_name='蒸気単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_gas = models.FloatField(verbose_name='ガス単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_water = models.FloatField(verbose_name='水単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent0 = models.FloatField(verbose_name='溶剤0単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent1 = models.FloatField(verbose_name='溶剤1単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent2 = models.FloatField(verbose_name='溶剤2単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent3 = models.FloatField(verbose_name='溶剤3単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent4 = models.FloatField(verbose_name='溶剤4単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent5 = models.FloatField(verbose_name='溶剤5単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent6 = models.FloatField(verbose_name='溶剤6単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent7 = models.FloatField(verbose_name='溶剤7単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent8 = models.FloatField(verbose_name='溶剤8単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Unit_price_solvent9 = models.FloatField(verbose_name='溶剤9単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    
    Cost_electric = models.FloatField(verbose_name='電力費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_steam = models.FloatField(verbose_name='蒸気費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_gas = models.FloatField(verbose_name='ガス費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_water = models.FloatField(verbose_name='水費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent0 = models.FloatField(verbose_name='溶剤費用0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent1 = models.FloatField(verbose_name='溶剤費用1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent2 = models.FloatField(verbose_name='溶剤費用2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent3 = models.FloatField(verbose_name='溶剤費用3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent4 = models.FloatField(verbose_name='溶剤費用4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent5 = models.FloatField(verbose_name='溶剤費用5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent6 = models.FloatField(verbose_name='溶剤費用6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent7 = models.FloatField(verbose_name='溶剤費用7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent8 = models.FloatField(verbose_name='溶剤費用8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent9 = models.FloatField(verbose_name='溶剤費用9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_electric = models.FloatField(verbose_name='合計費用（電力）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_steam = models.FloatField(verbose_name='合計費用（蒸気）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_gas = models.FloatField(verbose_name='合計費用（ガス）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_water = models.FloatField(verbose_name='合計費用（水）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent0 = models.FloatField(verbose_name='合計費用（溶剤0）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent1 = models.FloatField(verbose_name='合計費用（溶剤1）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent2 = models.FloatField(verbose_name='合計費用（溶剤2）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent3 = models.FloatField(verbose_name='合計費用（溶剤3）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent4 = models.FloatField(verbose_name='合計費用（溶剤4）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent5 = models.FloatField(verbose_name='合計費用（溶剤5）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent6 = models.FloatField(verbose_name='合計費用（溶剤6）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent7 = models.FloatField(verbose_name='合計費用（溶剤7）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent8 = models.FloatField(verbose_name='合計費用（溶剤8）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_solvent9 = models.FloatField(verbose_name='合計費用（溶剤9）',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total_all = models.FloatField(verbose_name='合計費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Data_date =  models.DateField(verbose_name='データ取得日（年月日）',blank=True,null=True)
    Data_time =  models.TimeField(verbose_name='データ取得日（時分秒）',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)



    def __str__(self):
       return str(self.Customer_machine_recipe)

    class Meta:
        verbose_name_plural = ('稼働履歴')







#電気コスト
class Cost_Electric(models.Model):
    Machine_drive_history = models.ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴',related_name='cost_history_electric')
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_electric = models.FloatField(verbose_name='電力費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
  

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 電力費用 : ' + str(self.Cost_electric) + \
                ' データ取得日 : ' + str(self.Data_datetime) + \
                    ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('電力コスト')


#蒸気コスト
class Cost_Steam(models.Model):
    Cost_id = models.IntegerField(verbose_name='蒸気コストID',default=0,blank=True,null=True)
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_steam = ForeignKey(Unit_Price_Steam,on_delete=CASCADE,verbose_name='単価')
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_steam = models.FloatField(verbose_name='蒸気費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 単価 : ' + str(self.Unit_price_steam) + \
                ' 蒸気費用 : ' + str(self.Cost_steam) + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('蒸気コスト')


#ガスコスト
class Cost_Gas(models.Model):
    Cost_id = models.IntegerField(verbose_name='ガスコストID',default=0,blank=True,null=True)
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_gas = ForeignKey(Unit_Price_Gas,on_delete=CASCADE,verbose_name='単価')
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_gas = models.FloatField(verbose_name='ガス費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 単価 : ' + str(self.Unit_price_gas) + \
                ' ガス費用 : ' + str(self.Cost_gas) + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('ガスコスト')


#水コスト
class Cost_Water(models.Model):
    Cost_id = models.IntegerField(verbose_name='水コストID',default=0,blank=True,null=True)
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_water = ForeignKey(Unit_Price_Water,on_delete=CASCADE,verbose_name='単価')
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_water = models.FloatField(verbose_name='水費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 単価 : ' + str(self.Unit_price_water) + \
                ' 水費用 : ' + str(self.Cost_water) + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('水コスト')


#溶剤コスト
class Cost_Solvent(models.Model):
    Cost_id = models.IntegerField(verbose_name='溶剤コストID',default=0,blank=True,null=True)
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Solvent0_conf = ForeignKey(Solvent0_Conf,on_delete=CASCADE,verbose_name='単価')
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent = models.FloatField(verbose_name='溶剤費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 単価 : ' + str(self.Solvent0_conf) + \
                ' 溶剤費用 : ' + str(self.Cost_solvent) + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('溶剤コスト')


#トータルコスト
class Cost_Total(models.Model):
    Cost_id = models.IntegerField(verbose_name='トータルコストID',default=0,blank=True,null=True)
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=models.SET_NULL,null=True,verbose_name='稼働履歴')
    Cost_electric = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_steam = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_gas = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_water = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_solvent = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Cost_total = models.FloatField(verbose_name='合計費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 合計費用 : ' + self.Cost_total + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('トータルコスト')


#装置温度ログ
class Machine_Temperature_Log(models.Model):
    Customer_machine_recipe = models.ForeignKey(Customer_Machine_Recipe,on_delete=CASCADE,verbose_name='コース名')
    Machine_log_temp0 = models.IntegerField(verbose_name='温度0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp1 = models.IntegerField(verbose_name='温度1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp2 = models.IntegerField(verbose_name='温度2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp3 = models.IntegerField(verbose_name='温度3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp4 = models.IntegerField(verbose_name='温度4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp5 = models.IntegerField(verbose_name='温度5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp6 = models.IntegerField(verbose_name='温度6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp7 = models.IntegerField(verbose_name='温度7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp8 = models.IntegerField(verbose_name='温度8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp9 = models.IntegerField(verbose_name='温度9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp10 = models.IntegerField(verbose_name='温度10',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_temp11 = models.IntegerField(verbose_name='温度11',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Data_date =  models.DateField(verbose_name='データ取得日（年月日）',blank=True,null=True)
    Data_time =  models.TimeField(verbose_name='データ取得日（時分秒）',blank=True,null=True)
    Machine_temp_log_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Machine_temp_log_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)

    def __str__(self):
       return str(self.Machine_model)

    class Meta:
        verbose_name_plural = ('温度log')

#装置稼働log
class Machine_Log(models.Model):
    Machine_model = models.ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Machine_log_time0 = models.BigIntegerField(verbose_name='稼働時間0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time1 = models.BigIntegerField(verbose_name='稼働時間1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time2 = models.BigIntegerField(verbose_name='稼働時間2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time3 = models.BigIntegerField(verbose_name='稼働時間3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time4 = models.BigIntegerField(verbose_name='稼働時間4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time5 = models.BigIntegerField(verbose_name='稼働時間5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time6 = models.BigIntegerField(verbose_name='稼働時間6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time7 = models.BigIntegerField(verbose_name='稼働時間7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time8 = models.BigIntegerField(verbose_name='稼働時間8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_time9 = models.BigIntegerField(verbose_name='稼働時間9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)    
    Machine_log_count0 = models.BigIntegerField(verbose_name='稼働回数0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count1 = models.BigIntegerField(verbose_name='稼働回数1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count2 = models.BigIntegerField(verbose_name='稼働回数2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count3 = models.BigIntegerField(verbose_name='稼働回数3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count4 = models.BigIntegerField(verbose_name='稼働回数4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count5 = models.BigIntegerField(verbose_name='稼働回数5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count6 = models.BigIntegerField(verbose_name='稼働回数6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count7 = models.BigIntegerField(verbose_name='稼働回数7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count8 = models.BigIntegerField(verbose_name='稼働回数8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_log_count9 = models.BigIntegerField(verbose_name='稼働回数9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Data_date =  models.DateField(verbose_name='データ取得日（年月日）',blank=True,null=True)
    Data_time =  models.TimeField(verbose_name='データ取得日（時分秒）',blank=True,null=True)
    Machine_log_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Machine_log_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)

    def __str__(self):
       return str(self.Machine_model)

    class Meta:
        verbose_name_plural = ('装置稼働log')


#PLC出力ログ
class Plc_Output_Count_Log(models.Model):
    Machine_model = models.ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Plc_count_log_output0 = models.BigIntegerField(verbose_name='OUT:0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output1 = models.BigIntegerField(verbose_name='OUT:1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output2 = models.BigIntegerField(verbose_name='OUT:2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output3 = models.BigIntegerField(verbose_name='OUT:3',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output4 = models.BigIntegerField(verbose_name='OUT:4',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output5 = models.BigIntegerField(verbose_name='OUT:5',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output6 = models.BigIntegerField(verbose_name='OUT:6',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output7 = models.BigIntegerField(verbose_name='OUT:7',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output8 = models.BigIntegerField(verbose_name='OUT:8',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output9 = models.BigIntegerField(verbose_name='OUT:9',validators=[MinValueValidator(0)],default=0,blank=True,null=True)

    Plc_count_log_output10 = models.BigIntegerField(verbose_name='OUT:10',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output11 = models.BigIntegerField(verbose_name='OUT:11',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output12 = models.BigIntegerField(verbose_name='OUT:12',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output13 = models.BigIntegerField(verbose_name='OUT:13',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output14 = models.BigIntegerField(verbose_name='OUT:14',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output15 = models.BigIntegerField(verbose_name='OUT:15',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output16 = models.BigIntegerField(verbose_name='OUT:16',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output17 = models.BigIntegerField(verbose_name='OUT:17',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output18 = models.BigIntegerField(verbose_name='OUT:18',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output19 = models.BigIntegerField(verbose_name='OUT:19',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    
    Plc_count_log_output20 = models.BigIntegerField(verbose_name='OUT:20',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output21 = models.BigIntegerField(verbose_name='OUT:21',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output22 = models.BigIntegerField(verbose_name='OUT:22',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output23 = models.BigIntegerField(verbose_name='OUT:23',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output24 = models.BigIntegerField(verbose_name='OUT:24',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output25 = models.BigIntegerField(verbose_name='OUT:25',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output26 = models.BigIntegerField(verbose_name='OUT:26',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output27 = models.BigIntegerField(verbose_name='OUT:27',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output28 = models.BigIntegerField(verbose_name='OUT:28',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output29 = models.BigIntegerField(verbose_name='OUT:29',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    
    Plc_count_log_output30 = models.BigIntegerField(verbose_name='OUT:30',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output31 = models.BigIntegerField(verbose_name='OUT:31',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output32 = models.BigIntegerField(verbose_name='OUT:32',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output33 = models.BigIntegerField(verbose_name='OUT:33',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output34 = models.BigIntegerField(verbose_name='OUT:34',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output35 = models.BigIntegerField(verbose_name='OUT:35',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output36 = models.BigIntegerField(verbose_name='OUT:36',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output37 = models.BigIntegerField(verbose_name='OUT:37',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output38 = models.BigIntegerField(verbose_name='OUT:38',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output39 = models.BigIntegerField(verbose_name='OUT:39',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    
    Plc_count_log_output40 = models.BigIntegerField(verbose_name='OUT:40',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output41 = models.BigIntegerField(verbose_name='OUT:41',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output42 = models.BigIntegerField(verbose_name='OUT:42',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output43 = models.BigIntegerField(verbose_name='OUT:43',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output44 = models.BigIntegerField(verbose_name='OUT:44',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output45 = models.BigIntegerField(verbose_name='OUT:45',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output46 = models.BigIntegerField(verbose_name='OUT:46',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output47 = models.BigIntegerField(verbose_name='OUT:47',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output48 = models.BigIntegerField(verbose_name='OUT:48',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output49 = models.BigIntegerField(verbose_name='OUT:49',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    
    Plc_count_log_output50 = models.BigIntegerField(verbose_name='OUT:50',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output51 = models.BigIntegerField(verbose_name='OUT:51',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output52 = models.BigIntegerField(verbose_name='OUT:52',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output53 = models.BigIntegerField(verbose_name='OUT:53',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output54 = models.BigIntegerField(verbose_name='OUT:54',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output55 = models.BigIntegerField(verbose_name='OUT:55',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output56 = models.BigIntegerField(verbose_name='OUT:56',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output57 = models.BigIntegerField(verbose_name='OUT:57',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output58 = models.BigIntegerField(verbose_name='OUT:58',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output59 = models.BigIntegerField(verbose_name='OUT:59',validators=[MinValueValidator(0)],default=0,blank=True,null=True)

    Plc_count_log_output60 = models.BigIntegerField(verbose_name='OUT:60',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output61 = models.BigIntegerField(verbose_name='OUT:61',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output62 = models.BigIntegerField(verbose_name='OUT:62',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Plc_count_log_output63 = models.BigIntegerField(verbose_name='OUT:63',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Data_date =  models.DateField(verbose_name='データ取得日（年月日）',blank=True,null=True)
    Data_time =  models.TimeField(verbose_name='データ取得日（時分秒）',blank=True,null=True)
    Plc_count_log_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Plc_count_log_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)

    def __str__(self):
       return str(self.Machine_model)

    class Meta:
        verbose_name_plural = ('PLC出力回数log')


#通知メール登録
class Mail_Notification(models.Model):
    Mail_name = models.CharField(verbose_name='氏名',max_length=20,blank=True,null=True)
    Mail_department = models.CharField(verbose_name='部署',max_length=20,blank=True,null=True)
    Mail_address = models.EmailField(max_length=240)
    Mail_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Mail_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
        return ' 氏名 : ' + self.Mail_name + \
                ' Email : ' + str(self.Mail_address)

    class Meta:
        verbose_name_plural = ('通知メール登録')


#異常メール設定
class Trouble_Mail_Setting(models.Model):
    Trouble_contents = ForeignKey(Trouble_Contents,on_delete=CASCADE,verbose_name='異常')
    Trouble_mail_notification = ForeignKey(Mail_Notification,on_delete=CASCADE,verbose_name='メール設定')
    Trouble_mail_send_setting = models.BooleanField(verbose_name='送信設定')
    Trouble_mail_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Trouble_mail_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
  
    def __str__(self):
        return '<id=' + str(self.id) + ', ' + \
            ' 異常 : ' + str(self.Trouble_contents) + \
                ' 通知メール設定 : ' + str(self.Trouble_mail_notification) + \
                    ' 送信設定 : ' + self.Trouble_mail_send_setting + \
                '>'

    class Meta:
        verbose_name_plural = ('異常メール設定')

#メンテナンスメール設定
class Maintenance_Mail_Setting(models.Model):
    Maintenance_machine_history = ForeignKey(Machine_Log,on_delete=CASCADE,verbose_name='稼働履歴')
    Maintenance_mail_notification = ForeignKey(Mail_Notification,on_delete=CASCADE,verbose_name='メール設定')
    Maintenance_threshold_time = models.IntegerField(verbose_name='閾値:時間',validators=[MinValueValidator(1)],default=1,blank=True,null=True)
    Maintenance_threshold_count = models.IntegerField(verbose_name='閾値:回数',validators=[MinValueValidator(1)],default=1,blank=True,null=True)
    Maintenance_send_setting = models.BooleanField(verbose_name='送信設定')
    Maintenance_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Maintenance_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
  
    def __str__(self):
        return '<id=' + str(self.id) + ', ' + \
            ' 稼働履歴 : ' + str(self.Maintenance_machine_history) + \
                ' 通知メール設定 : ' + str(self.Maintenance_mail_notification) + \
                    ' 閾値 : ' + str(self.Maintenance_threshold) + \
                        ' 送信設定 : ' + self.Maintenance_send_setting + \
                '>'

    class Meta:
        verbose_name_plural = ('メンテナンスメール設定')
