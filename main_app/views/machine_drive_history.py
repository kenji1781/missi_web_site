from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Machine_Recipe,Customer_Machine,Machine_Drive_History,\
    Unit_Price_Electric,Unit_Price_Steam,Unit_Price_Gas,Unit_Price_Water,Solvent0_Conf
from ..forms import MachineDriveHistoryCreateForm,MachineDriveHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class MachineDriveHistoryView(ListView):
    
    template_name = 'monitoring/machine_drive_history.html'
    model = Machine_Drive_History
    paginate_by = 10
    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '稼働履歴'
        ctx['msg'] = '稼働履歴の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Machine_Drive_History.objects.filter(\
                    Q(Customer_machine_id__contains=q_word)|Q(Customer_machine_id__icontains=q_word)|\
                        Q(Machine_model__contains=q_word)|Q(Machine_model__icontains=q_word))        
       
        elif q_date:
            object_list = Machine_Drive_History.objects.filter(\
                Q(Data_datetime__contains=q_date)|\
                    Q(Data_datetime__icontains=q_date)|\
                        Q(Machine_history_input_date__contains=q_date)|\
                            Q(Machine_history_input_date__icontains=q_date))
                       
        else:
            object_list = Machine_Drive_History.objects.order_by('-Machine_history_input_date')
            #各単価読み込み
            e_price = Unit_Price_Electric.objects.all().order_by('-Unit_price_electric_input_date').first()
            s_price = Unit_Price_Steam.objects.all().order_by('-Unit_price_steam_input_date').first()
            g_price = Unit_Price_Gas.objects.all().order_by('-Unit_price_gas_input_date').first()
            w_price = Unit_Price_Water.objects.all().order_by('-Unit_price_water_input_date').first()
            s0_price = Solvent0_Conf.objects.all().order_by('-Solvent0_input_date').first()
            
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


        return object_list
################################################################################
class MachineDriveHistoryCreateView(CreateView):
    

    template_name = 'monitoring/machine_drive_history_create.html'
    model = Machine_Drive_History
    form_class = MachineDriveHistoryCreateForm
    
    success_url = reverse_lazy("main_app:machine_drive_history") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '稼働履歴'
        ctx['msg'] = '稼働履歴の登録が出来ます。'
        return ctx
    
################################################################################
class MachineDriveHistoryUpdateView(UpdateView):

    template_name = 'monitoring/machine_drive_history_update.html'
    model = Machine_Drive_History
    form_class = MachineDriveHistoryUpdateForm
    
    success_url = reverse_lazy("main_app:machine_drive_history") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '稼働履歴'
        ctx['msg'] = '稼働履歴の変更が出来ます。'
        return ctx

################################################################################
class MachineDriveHistoryDeleteView(DeleteView):
    

    template_name = 'monitoring/machine_drive_history_delete.html'
    model = Machine_Drive_History
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:machine_drive_history")
 
