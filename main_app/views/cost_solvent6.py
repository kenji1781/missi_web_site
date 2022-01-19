from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Drive_History
from django.db .models import Q
from django.contrib import messages
from django.db.models import Count,Sum,Avg,Min,Max
from datetime import datetime,date,time
from ..machine_drive_history_model_comp import ModelComplement
#from django.utils.timezone import localdate,localtime

################################################################################
class CostSolvent6View(ListView):
    
    template_name = 'running_cost/cost_solvent6.html'
    model = Machine_Drive_History
    paginate_by = 50
    
    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤6コスト'
        ctx['msg'] = '溶剤6コスト確認が出来ます。'
        q_word = self.request.GET.get('query_text')
        q_date_f = self.request.GET.get('query_date_f')
        q_date_l = self.request.GET.get('query_date_l')
        if q_word and q_date_f and q_date_l:
            e_cost_total = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Sum('Cost_solvent6'))    #Q(Machine_drive_history__Machine_model__contains=q_word)|Q(Machine_drive_history__Machine_model__icontains=q_word))
            e_cost_avg = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Avg('Cost_solvent6'))
            e_cost_max = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Max('Cost_solvent6'))
            e_cost_min = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Min('Cost_solvent6'))
        
        
        else:
            e_cost_total = Machine_Drive_History.objects.all().aggregate(Sum('Cost_solvent6'))
            e_cost_avg = Machine_Drive_History.objects.all().aggregate(Avg('Cost_solvent6'))
            e_cost_max = Machine_Drive_History.objects.all().aggregate(Max('Cost_solvent6'))
            e_cost_min = Machine_Drive_History.objects.all().aggregate(Min('Cost_solvent6'))
        
        ctx.update(**e_cost_total)
        ctx.update(**e_cost_avg)
        ctx.update(**e_cost_max)
        ctx.update(**e_cost_min)
        
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date_f = self.request.GET.get('query_date_f')
        q_date_l = self.request.GET.get('query_date_l')

        if q_word and q_date_f and q_date_l:
            object_list = Machine_Drive_History.objects.filter(Customer_machine_id=q_word).filter(Data_datetime__range=(q_date_f, q_date_l))
                
            
        else:
            object_list = Machine_Drive_History.objects.all().order_by('-Data_datetime')    #.values('Customer_machine_id','Machine_model','Customer_machine_unit_no','Cost_electric','Data_datetime')
            
            modelcomp = ModelComplement()
            #datetimeをdateとtimeに分割
            modelcomp.datetime_complement(object_list)
            #idから機種を書込み
            modelcomp.machine_model_complement(object_list)
            #各最新単価を書込み
            modelcomp.unit_cost_complement(object_list)
           
            
        return object_list
            
            
        
   