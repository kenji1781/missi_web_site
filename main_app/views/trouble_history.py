from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Trouble_History,Customer_Machine,Trouble_Contents
from ..forms import TroubleHistoryCreateForm,TroubleHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages
from datetime import datetime,date,time
from ..plugin_plotly import GraphGenerator
import numpy as np
import pandas as pd
from django_pandas.io import read_frame



################################################################################
class TroubleHistoryView(ListView):
    
    template_name = 'monitoring/trouble_history.html'
    model = Trouble_History
    paginate_by = 50

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の確認／変更が出来ます。'
               
        return ctx
        

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date_f = self.request.GET.get('query_date_f')
        q_date_l = self.request.GET.get('query_date_l')

        if q_word and q_date_f and q_date_l:
            object_list = Trouble_History.objects.filter(Customer_machine_id=q_word).filter(Trouble_occurrence_time__range=(q_date_f, q_date_l))
                
            
        else:
            object_list = Trouble_History.objects.all().order_by('-Trouble_occurrence_time')    #.values('Customer_machine_id','Machine_model','Customer_machine_unit_no','Cost_electric','Data_datetime')

            for history in object_list:
                if (history.Trouble_occurrence_time != None)and(history.Trouble_recovery_time != None):
                    date1 = history.Trouble_recovery_time    
                    date2 = history.Trouble_occurrence_time
                    loss_time = date1-date2
                    history.time_calc = loss_time.total_seconds()
                    history.Trouble_loss_time = str(loss_time)
                    history.save()

                if (history.Customer_machine_id != None)and(history.Machine_model == None):
                    for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                        #for t_contents in Trouble_Contents.objects.select_related('Machine_model').all():
                        if history.Customer_machine_id == history.Customer_machine_id:
                                history.Machine_model = str(c_machine.Machine_model)+ ': #' +str(c_machine.Customer_machine_unit_no)                   
                                history.save()
                
                if (history.Trouble_no != None)and(history.Trouble_contents == None):
                    for t_contents in Trouble_Contents.objects.select_related('Machine_model').all():
                         if history.Trouble_no == t_contents.Trouble_no:
                                history.Trouble_contents = t_contents.Trouble_contents                   
                                history.save()        
                

        return object_list
################################################################################
class TroubleHistoryCreateView(CreateView):
    

    template_name = 'monitoring/trouble_history_create.html'
    model = Trouble_History
    form_class = TroubleHistoryCreateForm
    
    success_url = reverse_lazy("main_app:trouble_history") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の登録が出来ます。'
        return ctx
    
################################################################################
class TroubleHistoryUpdateView(UpdateView):

    template_name = 'monitoring/trouble_history_update.html'
    model = Trouble_History
    form_class = TroubleHistoryUpdateForm
    
    success_url = reverse_lazy("main_app:trouble_history") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の変更が出来ます。'
        return ctx

################################################################################
class TroubleHistoryDeleteView(DeleteView):
    

    template_name = 'monitoring/trouble_history_delete.html'
    model = Trouble_History
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:trouble_history") 
 
