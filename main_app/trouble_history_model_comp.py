from .models import Customer_Machine,Trouble_Contents
from datetime import datetime,date,time


class ModelComplement:
    """ビューから呼び出されて、モデルを補完する"""
    def trouble_history_model_complement(self,object):
        #ロスタイム補完
        for history in object:
            
            if (history.Trouble_occurrence_time != None)and(history.Trouble_recovery_time != None):
                try:
                    date1 = history.Trouble_recovery_time    
                    date2 = history.Trouble_occurrence_time
                    loss_time = date1-date2
                    history.time_calc = loss_time.total_seconds()
                    history.Trouble_loss_time = str(loss_time)
                    history.save()
                except:
                    pass
"""    
            if (history.Customer_machine_id != None)and(history.Machine_model == None):
                for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                    #for t_contents in Trouble_Contents.objects.select_related('Machine_model').all():
                    if history.Customer_machine_id == c_machine.Customer_machine_id:
                        try:
                            history.Machine_model = str(c_machine.Machine_model)+ ': #' +str(c_machine.Customer_machine_unit_no)                   
                            history.save()
                        except:
                            pass
            
            if (history.Trouble_no != None)and(history.Trouble_contents == None):
                for t_contents in Trouble_Contents.objects.select_related('Machine_model').all():
                    if history.Trouble_no == t_contents.Trouble_no:
                        try:
                            history.Trouble_contents = t_contents.Trouble_contents                   
                            history.save() 
                        except:
                            pass
"""      