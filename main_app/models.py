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
       return str(self.Machine_model) + ': #' +\
            str(self.Customer_machine_unit_no)

    class Meta:
        verbose_name_plural = ('客先装置')


#異常内容
class Trouble_Contents(models.Model):
    Machine_model = models.ForeignKey(Customer_Machine,on_delete=CASCADE,verbose_name='装置')
    Trouble_no = models.IntegerField(verbose_name='異常No',validators=[MinValueValidator(0)],blank=False,null=False)
    Trouble_contents = models.CharField(verbose_name='異常項目',max_length=20,blank=False,null=False)
    Trouble_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Trouble_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    

    def __str__(self):
       return str(self.Trouble_contents)
    
    class Meta:
        verbose_name_plural = ('異常内容')
        constraints = [
            models.UniqueConstraint(fields=['Machine_model','Trouble_no'],name='unique_trouble_no'),
        ]

#異常履歴 PLCより装置ID・異常No・発生時刻・復帰時刻を書き込む。
#装置ID・異常Noを基に型式・号機・異常項目を照合する。
class Trouble_History(models.Model):
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Trouble_no = models.IntegerField(verbose_name='異常No',validators=[MinValueValidator(0)],blank=True,null=True)
    Trouble_contents = models.CharField(verbose_name='異常項目',max_length=20,blank=True,null=True)
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

#品種名
class Recipe_Name(models.Model):
    Recipe_id = models.IntegerField(verbose_name='品種ID',validators=[MinValueValidator(0)],default=1,blank=True,null=True)
    Racipe_name = models.CharField(verbose_name='品種名',max_length=20,blank=True,null=True)
    Racipe_name_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
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
    Setting_item_id = models.IntegerField(verbose_name='品種ID',validators=[MinValueValidator(0)],blank=True,null=True,unique=True)
    Setting_item_name = models.CharField(verbose_name='品種名',max_length=20,blank=True,null=True,unique=True)
    Setting_item_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Setting_item_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 設定項目ID : ' + str(self.Setting_item_id) + \
            ' 設定項目 : ' + str(self.Setting_item_name) + \
        '>'

    class Meta:
        verbose_name_plural = ('設定項目')
        

#レシピ
class Customer_Machine_Recipe(models.Model):
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Recipe_id = models.IntegerField(verbose_name='品種ID',default=1,blank=True,null=True)
    Recipe_name = models.CharField(verbose_name='品種名',max_length=20,blank=True,null=True)
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
    Customer_machine_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Customer_machine_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)



    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 品種No : ' + str(self.Recipe_id) + \
            ' 品種名 : ' + str(self.Recipe_name)+ \
        '>'

    class Meta:
        verbose_name_plural = ('レシピ情報')


#装置稼働履歴
class Machine_Drive_History(models.Model):
    Customer_machine_id = models.IntegerField(verbose_name='装置ID',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    Machine_model = models.CharField(verbose_name='型式',max_length=20,blank=True,null=True)
    Customer_recipe_no = models.IntegerField(verbose_name='品種No',validators=[MinValueValidator(0)],default=1,blank=False,null=False)
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
    Data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    Data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    Data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    Data_date_hour = models.IntegerField(verbose_name='時',validators=[MinValueValidator(0),MaxValueValidator(24)],default=0,blank=True,null=True)
    Data_date_min = models.IntegerField(verbose_name='分',validators=[MinValueValidator(0),MaxValueValidator(59)],default=0,blank=True,null=True)
    Data_date_sec = models.IntegerField(verbose_name='秒',validators=[MinValueValidator(0),MaxValueValidator(59)],default=0,blank=True,null=True)
    Data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=False,null=False)
    Machine_history_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)
    Signal_sys_to_plc = models.BooleanField(default=False)
    Signal_plc_to_sys = models.BooleanField(default=False)



    def __str__(self):
       return str(self.Customer_machine_id) + str(self.Machine_model)+\
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


#設定:溶剤
class Solvent_Conf(models.Model):
    Solvent_name = models.ForeignKey(Solvent_Name,on_delete=CASCADE,verbose_name='溶剤名',related_name='solvent_name')
    Solvent_manu = models.ForeignKey(Solvent_Manufacturer,on_delete=CASCADE,verbose_name='メーカー',related_name='solvent_manu')
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
    Machine_history_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
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
#通知メール登録
class Mail_Notification(models.Model):
    Mail_name = models.CharField(verbose_name='氏名',max_length=20,blank=True,null=True)
    Mail_department = models.CharField(verbose_name='部署',max_length=20,blank=True,null=True)
    Mail_address = models.EmailField(max_length=240)
    Mail_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
    Mail_memo = models.TextField(verbose_name='メモ',blank=True,null=True,max_length=50)

    def __str__(self):
        return '<id=' + str(self.id) + ', ' + \
            ' 氏名 : ' + self.Mail_name + \
                ' Email : ' + str(self.Mail_address) + \
                    ' 登録日 : ' + str(self.Mail_input_date) + \
                '>'

    class Meta:
        verbose_name_plural = ('通知メール登録')


#異常メール設定
class Trouble_Mail_Setting(models.Model):
    Trouble_contents = ForeignKey(Trouble_Contents,on_delete=CASCADE,verbose_name='異常')
    Trouble_mail_notification = ForeignKey(Mail_Notification,on_delete=CASCADE,verbose_name='メール設定')
    Trouble_mail_send_setting = models.BooleanField(verbose_name='送信設定')
    Trouble_mail_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
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
    Maintenance_machine_history = ForeignKey(Machine_Drive_History,on_delete=CASCADE,verbose_name='稼働履歴')
    Maintenance_mail_notification = ForeignKey(Mail_Notification,on_delete=CASCADE,verbose_name='メール設定')
    Maintenance_threshold = models.IntegerField(verbose_name='閾値',validators=[MinValueValidator(1)],default=1,blank=True,null=True)
    Maintenance_send_setting = models.BooleanField(verbose_name='送信設定')
    Maintenance_input_date = models.DateField(verbose_name='登録日',blank=True,null=True)
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
