from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Temperature_Log
from ..forms import MachineTemperatureLogCreateForm,MachineTemperatureLogUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


################################################################################
class MachineTemperatureLogView(LoginRequiredMixin,ListView):
    
    template_name = 'monitoring/machine_temperature_log.html'
    model = Machine_Temperature_Log
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '温度監視'
        ctx['msg'] = '温度の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Machine_Temperature_Log.objects.select_related('Customer_machine_recipe').filter(Q(Customer_machine_recipe__Machine_model__Customer_machine_id__contains=q_word)|Q(Customer_machine_recipe__Machine_model__Customer_machine_id__icontains=q_word)|Q(Customer_machine_recipe__Machine_model__Machine_model__Machine_model__contains=q_word)|Q(Customer_machine_recipe__Machine_model__Machine_model__Machine_model__icontains=q_word))
        elif q_date:
            object_list = Machine_Temperature_Log.objects.select_related('Customer_machine_recipe').filter(Q(Machine_temp_log_input_date__icontains=q_date)|\
                Q(Machine_temp_log_input_date__icontains=q_date))
        else:
            object_list = Machine_Temperature_Log.objects.select_related('Customer_machine_recipe').order_by('-Machine_temp_log_input_date')


        return object_list
################################################################################
class MachineTemperatureLogCreateView(CreateView):
    

    template_name = 'monitoring/machine_temperature_log_create.html'
    model = Machine_Temperature_Log
    form_class = MachineTemperatureLogCreateForm
    
    success_url = reverse_lazy("main_app:machine_temperature_log") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '温度監視'
        ctx['msg'] = '温度の登録が出来ます。'
        return ctx
    
################################################################################
class MachineTemperatureLogUpdateView(UpdateView):

    template_name = 'monitoring/machine_temperature_log_update.html'
    model = Machine_Temperature_Log
    form_class = MachineTemperatureLogUpdateForm
    
    success_url = reverse_lazy("main_app:machine_temperature_log") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '温度監視'
        ctx['msg'] = '温度の変更が出来ます。'
        return ctx

################################################################################
class MachineTemperatureLogDeleteView(DeleteView):
    

    template_name = 'monitoring/machine_temperature_log_delete.html'
    model = Machine_Temperature_Log
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:machine_temperature_log") 
 
