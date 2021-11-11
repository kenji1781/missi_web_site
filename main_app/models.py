from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

# Create your models here.
class Machine_data(models.Model):
    machine_name = models.CharField(max_length=20,blank=True,null=False)  #装置名
    machine_unit_no = models.IntegerField(max_length=12,blank=True,null=False)    #号機
    machine_inst_date = models.DateField(blank=True,null=True)  #設置日

    #class Meta:
        #verbose_name_plural = 'Machine_data'

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		self.machine_name + '(' + str(self.machine_unit_no) + '),'\
			' inst_date :' + str(self.machine_inst_date) +'>'




class Machine_setting(models.Model):
    machine_data = models.ForeignKey(Machine_data,on_delete=CASCADE) #装置データ
    set_couse_no = models.IntegerField(max_length=3,blank=True,null=True) #コースNo
    
    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		self.machine_data + ' couse_no :' + str(self.set_couse_no) +'>'




class Machine_drive_data(models.Model):
    machine_setting = models.ForeignKey(Machine_setting,on_delete=CASCADE)
    machine_drying_time = models.IntegerField(default=0,blank=True,null=True)
    machine_drive_count = models.IntegerField(default=0,blank=True,null=True)
    machine_drive_time_m = models.IntegerField(default=0,blank=True,null=True)
    machine_drive_time_s = models.IntegerField(default=0,blank=True,null=True)
    machine_steam_used = models.IntegerField(default=0,blank=True,null=True)
    machine_electric_used = models.IntegerField(default=0,blank=True,null=True)
    machime_air_used = models.IntegerField(default=0,blank=True,null=True)
    machime_gas_used = models.IntegerField(default=0,blank=True,null=True)
    data_date_month = models.IntegerField(default=1,blank=True,null=True)
    data_date_day = models.IntegerField(default=1,blank=True,null=True)
    data_datetime =  models.DateTimeField(blank=True,null=True)

    def __str__(self):
       return '<id=' + str(self.id) + ', ' + \
		self.machine_setting + \
			' data_date :' + str(self.data_datetime) +'>'





class input_data(models.Model):
    input_date = models.DateTimeField()

