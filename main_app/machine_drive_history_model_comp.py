from .models import Customer_Machine,\
    Unit_Price_Electric,Unit_Price_Steam,Unit_Price_Gas,Unit_Price_Water,\
        Solvent0_Conf,Solvent1_Conf,Solvent2_Conf,Solvent3_Conf,Solvent4_Conf,Solvent5_Conf,Solvent6_Conf,Solvent7_Conf,Solvent8_Conf,Solvent9_Conf



class ModelComplement:
    """ビューから呼び出されて、モデルを補完する"""
    def machine_model_complement(self,object):
        #idから機種を書込み
        for history_i in object:
            if (history_i.Machine_model==None) and (history_i.Customer_machine_id != None):
                    for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                       if history_i.Customer_machine_id == c_machine.Customer_machine_id:
                            try:
                                history_i.Machine_model = str(c_machine.Machine_model)                   
                                history_i.save()
                            except:
                                pass
    
    def unit_cost_complement(self,object):
        #各単価読み込み
        e_price = Unit_Price_Electric.objects.all().order_by('-Unit_price_electric_input_date').first()
        s_price = Unit_Price_Steam.objects.all().order_by('-Unit_price_steam_input_date').first()
        g_price = Unit_Price_Gas.objects.all().order_by('-Unit_price_gas_input_date').first()
        w_price = Unit_Price_Water.objects.all().order_by('-Unit_price_water_input_date').first()
        s0_price = Solvent0_Conf.objects.all().order_by('-Solvent0_input_date').first()
        s1_price = Solvent1_Conf.objects.all().order_by('-Solvent1_input_date').first()
        s2_price = Solvent2_Conf.objects.all().order_by('-Solvent2_input_date').first()
        s3_price = Solvent3_Conf.objects.all().order_by('-Solvent3_input_date').first()
        s4_price = Solvent4_Conf.objects.all().order_by('-Solvent4_input_date').first()
        s5_price = Solvent5_Conf.objects.all().order_by('-Solvent5_input_date').first()
        s6_price = Solvent6_Conf.objects.all().order_by('-Solvent6_input_date').first()
        s7_price = Solvent7_Conf.objects.all().order_by('-Solvent7_input_date').first()
        s8_price = Solvent8_Conf.objects.all().order_by('-Solvent8_input_date').first()
        s9_price = Solvent9_Conf.objects.all().order_by('-Solvent9_input_date').first()
  
        #単価を書込み
        for history_i in object:
            #電力単価書き込み         
            if (history_i.Unit_price_electric==None)or(history_i.Unit_price_electric==0):
                try:
                    history_i.Unit_price_electric = e_price.Unit_price_electric
                    history_i.save()
                except:
                    pass
            #蒸気単価書き込み
            if (history_i.Unit_price_steam==None)or(history_i.Unit_price_steam==0):
                try:
                    history_i.Unit_price_steam = s_price.Unit_price_steam
                    history_i.save()
                except:
                    pass
            #ガス単価書き込み    
            if (history_i.Unit_price_gas==None)or(history_i.Unit_price_gas==0):
                try:
                    history_i.Unit_price_gas = g_price.Unit_price_gas
                    history_i.save()
                except:
                    pass
            #水単価書き込み
            if (history_i.Unit_price_water==None)or(history_i.Unit_price_water==0):
                try:
                    history_i.Unit_price_water = w_price.Unit_price_water
                    history_i.save()
                except:
                    pass
            #溶剤0単価書き込み
            if (history_i.Unit_price_solvent0==None)or(history_i.Unit_price_solvent0==0):
                try:
                    history_i.Unit_price_solvent0 = s0_price.Unit_price_solvent0
                    history_i.save()
                except:
                    pass
            #溶剤1単価書き込み
            if (history_i.Unit_price_solvent1==None)or(history_i.Unit_price_solvent1==0):
                try:
                    history_i.Unit_price_solvent1 = s1_price.Unit_price_solvent1
                    history_i.save()
                except:
                    pass
            #溶剤2単価書き込み
            if (history_i.Unit_price_solvent2==None)or(history_i.Unit_price_solvent2==0):
                try:
                    history_i.Unit_price_solvent2 = s2_price.Unit_price_solvent2
                    history_i.save()
                except:
                    pass
            #溶剤3単価書き込み
            if (history_i.Unit_price_solvent3==None)or(history_i.Unit_price_solvent3==0):
                try:
                    history_i.Unit_price_solvent3 = s3_price.Unit_price_solvent3
                    history_i.save()
                except:
                    pass
            #溶剤4単価書き込み
            if (history_i.Unit_price_solvent4==None)or(history_i.Unit_price_solvent4==0):
                try:
                    history_i.Unit_price_solvent4 = s4_price.Unit_price_solvent4
                    history_i.save()
                except:
                    pass
            #溶剤5単価書き込み
            if (history_i.Unit_price_solvent5==None)or(history_i.Unit_price_solvent5==0):
                try:
                    history_i.Unit_price_solvent5 = s5_price.Unit_price_solvent5
                    history_i.save()
                except:
                    pass
            #溶剤6単価書き込み
            if (history_i.Unit_price_solvent6==None)or(history_i.Unit_price_solvent6==0):
                try:
                    history_i.Unit_price_solvent6 = s6_price.Unit_price_solvent6
                    history_i.save()
                except:
                    pass
            #溶剤7単価書き込み
            if (history_i.Unit_price_solvent7==None)or(history_i.Unit_price_solvent7==0):
                try:
                    history_i.Unit_price_solvent7 = s7_price.Unit_price_solvent7
                    history_i.save()
                except:
                    pass
            #溶剤8単価書き込み
            if (history_i.Unit_price_solvent8==None)or(history_i.Unit_price_solvent8==0):
                try:
                    history_i.Unit_price_solvent8 = s8_price.Unit_price_solvent8
                    history_i.save()
                except:
                    pass
            #溶剤9単価書き込み
            if (history_i.Unit_price_solvent9==None)or(history_i.Unit_price_solvent9==0):
                try:
                    history_i.Unit_price_solvent9 = s9_price.Unit_price_solvent9
                    history_i.save()
                except:
                    pass
            
            #電力費用書き込み         
            if (history_i.Cost_electric==None)or(history_i.Cost_electric==0)and((history_i.Unit_price_electric>0)and(history_i.Machine_electric_used>0)):
                try:
                    history_i.Cost_electric = history_i.Unit_price_electric * history_i.Machine_electric_used
                    history_i.save()
                except:
                    pass
            
            #蒸気費用書き込み         
            if (history_i.Cost_steam==None)or(history_i.Cost_steam==0)and((history_i.Unit_price_steam>0)and(history_i.Machine_steam_used>0)):
                try:
                    history_i.Cost_steam = history_i.Unit_price_steam * history_i.Machine_steam_used
                    history_i.save()
                except:
                    pass
            
            #ガス費用書き込み         
            if (history_i.Cost_gas==None)or(history_i.Cost_gas==0)and((history_i.Unit_price_gas>0)and(history_i.Machine_gas_used>0)):
                try:
                    history_i.Cost_gas = history_i.Unit_price_gas * history_i.Machine_gas_used
                    history_i.save()
                except:
                    pass
            
            #水費用書き込み         
            if (history_i.Cost_water==None)or(history_i.Cost_water==0)and((history_i.Unit_price_water>0)and(history_i.Machine_water_used>0)):
                try:
                    history_i.Cost_water = history_i.Unit_price_water * history_i.Machine_water_used
                    history_i.save()
                except:
                    pass
    
            #溶剤0費用書き込み         
            if (history_i.Cost_solvent0==None)or(history_i.Cost_solvent0==0)and((history_i.Unit_price_solvent0>0)and(history_i.Machine_solvent0_used>0)):
                try:
                    history_i.Cost_solvent0 = history_i.Unit_price_solvent0 * history_i.Machine_solvent0_used
                    history_i.save()
                except:
                    pass

            #溶剤1費用書き込み         
            if (history_i.Cost_solvent1==None)or(history_i.Cost_solvent1==0)and((history_i.Unit_price_solvent1>0)and(history_i.Machine_solvent1_used>0)):
                try:
                    history_i.Cost_solvent1 = history_i.Unit_price_solvent1 * history_i.Machine_solvent1_used
                    history_i.save()
                except:
                    pass

            #溶剤2費用書き込み         
            if (history_i.Cost_solvent2==None)or(history_i.Cost_solvent2==0)and((history_i.Unit_price_solvent2>0)and(history_i.Machine_solvent2_used>0)):
                try:
                    history_i.Cost_solvent2 = history_i.Unit_price_solvent2 * history_i.Machine_solvent2_used
                    history_i.save()
                except:
                    pass

            #溶剤3費用書き込み         
            if (history_i.Cost_solvent3==None)or(history_i.Cost_solvent3==0)and((history_i.Unit_price_solvent3>0)and(history_i.Machine_solvent3_used>0)):
                try:
                    history_i.Cost_solvent3 = history_i.Unit_price_solvent3 * history_i.Machine_solvent3_used
                    history_i.save()
                except:
                    pass

            #溶剤4費用書き込み         
            if (history_i.Cost_solvent4==None)or(history_i.Cost_solvent4==0)and((history_i.Unit_price_solvent4>0)and(history_i.Machine_solvent4_used>0)):
                try:
                    history_i.Cost_solvent4 = history_i.Unit_price_solvent4 * history_i.Machine_solvent4_used
                    history_i.save()
                except:
                    pass

            #溶剤5費用書き込み         
            if (history_i.Cost_solvent5==None)or(history_i.Cost_solvent5==0)and((history_i.Unit_price_solvent5>0)and(history_i.Machine_solvent5_used>0)):
                try:
                    history_i.Cost_solvent5 = history_i.Unit_price_solvent5 * history_i.Machine_solvent5_used
                    history_i.save()
                except:
                    pass

            #溶剤6費用書き込み         
            if (history_i.Cost_solvent6==None)or(history_i.Cost_solvent6==0)and((history_i.Unit_price_solvent6>0)and(history_i.Machine_solvent6_used>0)):
                try:
                    history_i.Cost_solvent6 = history_i.Unit_price_solvent6 * history_i.Machine_solvent6_used
                    history_i.save()
                except:
                    pass

            #溶剤7費用書き込み         
            if (history_i.Cost_solvent7==None)or(history_i.Cost_solvent7==0)and((history_i.Unit_price_solvent7>0)and(history_i.Machine_solvent7_used>0)):
                try:
                    history_i.Cost_solvent7 = history_i.Unit_price_solvent7 * history_i.Machine_solvent7_used
                    history_i.save()
                except:
                    pass

            #溶剤8費用書き込み         
            if (history_i.Cost_solvent8==None)or(history_i.Cost_solvent8==0)and((history_i.Unit_price_solvent8>0)and(history_i.Machine_solvent8_used>0)):
                try:
                    history_i.Cost_solvent8 = history_i.Unit_price_solvent8 * history_i.Machine_solvent8_used
                    history_i.save()
                except:
                    pass

            #溶剤9費用書き込み         
            if (history_i.Cost_solvent9==None)or(history_i.Cost_solvent9==0)and((history_i.Unit_price_solvent9>0)and(history_i.Machine_solvent9_used>0)):
                try:
                    history_i.Cost_solvent9 = history_i.Unit_price_solvent9 * history_i.Machine_solvent9_used
                    history_i.save()
                except:
                    pass

    def datetime_complement(self,object):
        
        for history_i in object:
            #データ取得日　datetimeからdateを書込み
            if history_i.Data_datetime != None:
                date_r = history_i.Data_datetime.date()
                                
                if ((history_i.Data_datetime != None) and (history_i.Data_date == None))\
                        or (date_r != history_i.Data_date):
                    try:
                        history_i.Data_date = date_r
                        history_i.save()
                    except:
                        pass

            #データ取得日　datetimeからtimeを書込み
            if history_i.Data_datetime != None:
                time_r = history_i.Data_datetime.time()
                print(time_r)
                
                if ((history_i.Data_datetime != None) and (history_i.Data_time == None))\
                        or (time_r != history_i.Data_time):
                    try:
                        history_i.Data_time = time_r
                        history_i.save()
                    except:
                        pass
