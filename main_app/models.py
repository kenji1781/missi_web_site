from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from django.db.models.fields.related import ForeignKey


#メーカー登録情報#####################################################################

# 客先情報☆
class Customer_Infomation(models.Model):
    Customer_name = models.CharField(verbose_name='企業名',max_length=20,blank=True,null=False)
    
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    Customer_tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号',blank=True,null=True)
    
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
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
    Equipment_category = CharField(verbose_name='装置カテゴリー',max_length=10,blank=False,null=False)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		        ' 装置カテゴリー : '+ self.Equipment_category + '>'

    class Meta:
        verbose_name_plural = ('装置カテゴリー')


#装置型式☆
class Machine_Model(models.Model):
    Machine_category = models.ForeignKey(Equipment_Category,on_delete=CASCADE,verbose_name='装置カテゴリー')
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=False,null=False)
    Machine_model_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_model_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
           ' 型式: ' + self.Machine_model + \
                ' 登録日 : ' + str(self.Machine_model_input_date) + '>'

    class Meta:
        verbose_name_plural = ('装置型式')

#客先装置
class Customer_Machine(models.Model):
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
    Machine_model = models.ForeignKey(Machine_Model,on_delete=CASCADE,verbose_name='装置')
    Customer_machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=False,null=False)
    Customer_machine_inst_date = models.DateField(verbose_name='納入日',blank=True,null=True)
    Customer_machine_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Customer_machine_memo = models.TextField(verbose_name='メモ',blank=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 装置 : ' + str(self.Machine_model) + \
            '(' + str(self.Customer_machine_unit_no) + '),' +\
			' 納入日 : ' + str(self.Customer_machine_inst_date) +'>'

    class Meta:
        verbose_name_plural = ('客先装置')


#異常内容
class Trouble_Contents(models.Model):
    Machine_model = models.ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Trouble_no = models.IntegerField(verbose_name='異常No',validators=[MinValueValidator(0)],blank=False,null=False)
    Trouble_contents = models.CharField(verbose_name='異常',max_length=20,blank=False,null=False)
    Trouble_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Trouble_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		    ' 異常No : '+ str(self.Trouble_no) + \
                ' 異常 : ' + self.Trouble_contents + \
                    ' 異常内容 : ' + self.Trouble_memo + \
			'>'
    
    class Meta:
        verbose_name_plural = ('異常内容')

#異常履歴
class Trouble_History(models.Model):
    Trouble_contents = ForeignKey(Trouble_Contents,on_delete=CASCADE,verbose_name='異常')
    Trouble_occurrence_time = models.DateTimeField(verbose_name='発生時刻',blank=True,null=True)   
    Trouble_recovery_time = models.DateTimeField(verbose_name='復帰時刻',blank=True,null=True)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		    ' 異常 : ' + str(self.Trouble_contents) + \
                ' 発生時刻 : ' + str(self.Trouble_occurrence_time) + \
                    ' 復帰時刻 : ' + str(self.Trouble_recovery_time) + \
                 + '>'

    class Meta:
        verbose_name_plural = ('異常履歴')

#品種名
class Recipe_Name(models.Model):
    Recipe_id = models.IntegerField(verbose_name='品種ID',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
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


#レシピ
class Customer_Machine_Recipe(models.Model):
    Customer_racipe_name = ForeignKey(Recipe_Name,on_delete=CASCADE,verbose_name='品種')
    Customer_machine = ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
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
    Customer_machine_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Customer_machine_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 品種No : ' + str(self.Customer_recipe_no) + \
            ' 品種名 : ' + str(self.Customer_racipe_name)+ \
        '>'

    class Meta:
        verbose_name_plural = ('レシピ情報')


#装置稼働履歴
class Machine_Drive_History(models.Model):
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=False,null=False)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
    Machine_drive_time0 = models.IntegerField(verbose_name='運転時間0',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_time1 = models.IntegerField(verbose_name='運転時間1',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_drive_time2 = models.IntegerField(verbose_name='運転時間2',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
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
    Machine_drive_count = models.IntegerField(verbose_name='稼働回数',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_water_used = models.FloatField(verbose_name='水使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_steam_used = models.FloatField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_electric_used = models.FloatField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_gas_used = models.FloatField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 装置 : ' + str(self.Customer_machine_recipe) + \
            ' データ取得日 : ' + str(self.Data_datetime) + \
                ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('稼働履歴')



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
    Solvent_name = models.CharField(verbose_name='溶剤名',max_length=20,blank=True,null=True)
    
    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + self.Solvent_name  + '>'

    class Meta:
        verbose_name_plural = ('溶剤名')


#溶剤メーカー
class Solvent_Manufacturer(models.Model):
    Solvent_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤')
    Solvent_manu = models.CharField(verbose_name='メーカー',max_length=20,blank=True,null=True)
    
    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent_name) + \
            ' メーカー : ' + self.Solvent_manu + '>'

    class Meta:
        verbose_name_plural = ('溶剤メーカー')


#設定:溶剤
class Solvent_Conf(models.Model):
    Solvent_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='溶剤')
    Solvent_unit_price = models.FloatField(verbose_name='単価',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Solvent_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Solvent_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 溶剤名 : ' + str(self.Solvent_manu) + \
            ' 単価 : ' + str(self.Solvent_unit_price) + \
                ' 登録日 : ' + str(self.Solvent_input_date) + \
                ' メモ : ' + self.Solvent_memo + '>'

    class Meta:
        verbose_name_plural = ('溶剤設定')





#電気コスト
class Cost_Electric(models.Model):
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_electric = ForeignKey(Unit_Price_Electric,on_delete=CASCADE,verbose_name='単価')
    Cost_electric = models.FloatField(verbose_name='電力費用',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 稼働履歴 : ' + str(self.Machine_drive_history) + \
            ' 単価 : ' + str(self.Unit_price_electric) + \
                ' 電力費用 : ' + str(self.Cost_electric) + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('電力コスト')


#蒸気コスト
class Cost_Steam(models.Model):
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_steam = ForeignKey(Unit_Price_Steam,on_delete=CASCADE,verbose_name='単価')
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
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_gas = ForeignKey(Unit_Price_Gas,on_delete=CASCADE,verbose_name='単価')
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
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Unit_price_water = ForeignKey(Unit_Price_Water,on_delete=CASCADE,verbose_name='単価')
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
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Solvent_conf = ForeignKey(Solvent_Conf,on_delete=CASCADE,verbose_name='単価')
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
            ' 単価 : ' + str(self.Solvent_conf) + \
                ' 溶剤費用 : ' + str(self.Cost_solvent) + \
                    ' データ取得日 : ' + str(self.Data_datetime) + \
                        ' 登録日 : ' + str(self.Machine_history_input_date) + \
        '>'

    class Meta:
        verbose_name_plural = ('溶剤コスト')


#トータルコスト
class Cost_Total(models.Model):
    Machine_drive_history = ForeignKey(Machine_Drive_History,on_delete=models.SET_NULL,null=True,verbose_name='稼働履歴')
    Cost_electric = ForeignKey(Cost_Electric,on_delete=models.SET_NULL,null=True,verbose_name='電力費用')
    Cost_steam = ForeignKey(Cost_Steam,on_delete=models.SET_NULL,null=True,verbose_name='蒸気費用')
    Cost_gas = ForeignKey(Cost_Gas,on_delete=models.SET_NULL,null=True,verbose_name='ガス費用')
    Cost_water = ForeignKey(Cost_Water,on_delete=models.SET_NULL,null=True,verbose_name='水費用')
    Cost_solvent = ForeignKey(Cost_Solvent,on_delete=models.SET_NULL,null=True,verbose_name='溶剤費用')
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