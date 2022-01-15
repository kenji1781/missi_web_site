from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Machine_Recipe,Customer_Machine,Machine_Drive_History,\
    Unit_Price_Electric
from django.db .models import Q
from django.contrib import messages
from django.db.models import Count,Sum,Avg,Min,Max
from datetime import datetime,date,time
#from django.utils.timezone import localdate,localtime

################################################################################
class CostElectricView(ListView):
    
    template_name = 'running_cost/cost_electric.html'
    model = Machine_Drive_History
    paginate_by = 50
    
    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '電力コスト'
        ctx['msg'] = '電力コスト確認が出来ます。'
        q_word = self.request.GET.get('query_text')
        q_date_f = self.request.GET.get('query_date_f')
        q_date_l = self.request.GET.get('query_date_l')
        if q_word and q_date_f and q_date_l:
            e_cost_total = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Sum('Cost_electric'))    #Q(Machine_drive_history__Machine_model__contains=q_word)|Q(Machine_drive_history__Machine_model__icontains=q_word))
            e_cost_avg = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Avg('Cost_electric'))
            e_cost_max = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Max('Cost_electric'))
            e_cost_min = Machine_Drive_History.objects.all().filter(Customer_machine_id=q_word).filter(Data_date__range=(q_date_f, q_date_l)).aggregate(Min('Cost_electric'))
        
        
        else:
            e_cost_total = Machine_Drive_History.objects.all().aggregate(Sum('Cost_electric'))
            e_cost_avg = Machine_Drive_History.objects.all().aggregate(Avg('Cost_electric'))
            e_cost_max = Machine_Drive_History.objects.all().aggregate(Max('Cost_electric'))
            e_cost_min = Machine_Drive_History.objects.all().aggregate(Min('Cost_electric'))
        
        ctx.update(**e_cost_total)
        ctx.update(**e_cost_avg)
        ctx.update(**e_cost_max)
        ctx.update(**e_cost_min)
        
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date_f = self.request.GET.get('query_date_f')
        q_date_l = self.request.GET.get('query_date_l')

        if q_date_f and q_date_l:
            object_list = Machine_Drive_History.objects.filter(Data_datetime__range=(q_date_f, q_date_l))
                
            
        else:
            
        
            e_cost_total = Machine_Drive_History.objects.all().aggregate(Sum('Cost_electric'))
        
            object_list = Machine_Drive_History.objects.all().order_by('-Data_datetime')    #.values('Customer_machine_id','Machine_model','Customer_machine_unit_no','Cost_electric','Data_datetime')
            #各単価読み込み
            e_price = Unit_Price_Electric.objects.all().order_by('-Unit_price_electric_input_date').first()
            
            for history_i in object_list:
                #機種型式書き込み
                if (history_i.Machine_model==None) and (history_i.Customer_machine_id != None):
                    for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                        if history_i.Customer_machine_id == c_machine.Customer_machine_id:
                            history_i.Machine_model = str(c_machine.Machine_model)                   
                            history_i.save()
                #電力単価書き込み         
                if (history_i.Unit_price_electric==None)or(history_i.Unit_price_electric==0):
                    try:
                        history_i.Unit_price_electric = e_price.Unit_price_electric
                        history_i.save()
                    except:
                        pass
                #電力費用書き込み         
                try:
                    history_i.Cost_electric = history_i.Unit_price_electric * history_i.Machine_electric_used
                    history_i.save()
                except:
                    pass


                #データ取得日　datetimeからdateを書込み
                if history_i.Data_datetime != None:
                    date_r = history_i.Data_datetime.date()
                    print(date_r)
                
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

        
        
        return object_list


        
"""
################################################################################
class CostElectricCreateView(CreateView):
    

    template_name = 'monitoring/cost_electric_create.html'
    model = Machine_Drive_History
    #form_class = CostElectricCreateForm
    
    s#uccess_url = reverse_lazy("main_app:cost_electric") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '電力コスト'
        ctx['msg'] = '電力コストの登録が出来ます。'
        return ctx
    
################################################################################
class CostElectricUpdateView(UpdateView):

    template_name = 'monitoring/cost_electric_update.html'
    model = Cost_Electric
    form_class = CostElectricUpdateForm
    
    success_url = reverse_lazy("main_app:cost_electric") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '電力コスト'
        ctx['msg'] = '電力コスト登録の変更が出来ます。'
        return ctx

################################################################################
class CostElectricDeleteView(DeleteView):
    

    template_name = 'monitoring/cost_electric_delete.html'
    model = Cost_Electric
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:cost_electric") 
""" 
