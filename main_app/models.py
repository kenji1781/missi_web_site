from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Machine_data(models.Model):
    machine_name = models.CharField(verbose_name='装置名',max_length=20,blank=True,null=False)
    machine_unit_no = models.IntegerField(verbose_name='号機',validators=[MinValueValidator(1)],default=1,blank=True,null=False)
    machine_inst_date = models.DateField(verbose_name='納入日',blank=True,null=True)

    #class Meta:
        #verbose_name_plural = 'Machine_data'

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' 装置名 : '+self.machine_name + '(' + str(self.machine_unit_no) + '),'\
			' 納入日 : ' + str(self.machine_inst_date) +'>'




class Machine_setting(models.Model):
    machine_data = models.ForeignKey(Machine_data,on_delete=CASCADE)
    set_couse_no = models.IntegerField(verbose_name='コースNo',validators=[MinValueValidator(0)],blank=True,null=True)
    
    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' ' + str(self.machine_data) + ' コースNo : ' + str(self.set_couse_no) +'>'




class Machine_drive_data(models.Model):
    machine_setting = models.ForeignKey(Machine_setting,on_delete=CASCADE)
    machine_drying_time = models.IntegerField(verbose_name='乾燥時間',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machine_drive_count = models.IntegerField(verbose_name='稼働回数',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machine_drive_time_m = models.IntegerField(verbose_name='運転時間:分',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machine_drive_time_s = models.IntegerField(verbose_name='運転時間:秒',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machine_steam_used = models.IntegerField(verbose_name='蒸気使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machine_electric_used = models.IntegerField(verbose_name='電力使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machime_air_used = models.IntegerField(verbose_name='エア使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    machime_gas_used = models.IntegerField(verbose_name='ガス使用量',validators=[MinValueValidator(0)],default=0,blank=True,null=True)
    data_date_year = models.IntegerField(verbose_name='年',validators=[MinValueValidator(2021)],default=2021,blank=True,null=True)
    data_date_month = models.IntegerField(verbose_name='月',validators=[MinValueValidator(1),MaxValueValidator(12)],default=1,blank=True,null=True)
    data_date_day = models.IntegerField(verbose_name='日',validators=[MinValueValidator(1),MaxValueValidator(31)],default=1,blank=True,null=True)
    data_datetime =  models.DateTimeField(verbose_name='データ取得日',blank=True,null=True)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		' ' + str(self.machine_setting) + \
			' データ取得日 : ' + str(self.data_datetime) +'>'





class input_data(models.Model):
    input_date = models.DateTimeField()

