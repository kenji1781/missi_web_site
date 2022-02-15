from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Plc_Output_Count_Log
from ..forms import PlcOutputCountLogCreateForm,PlcOutputCountLogUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


################################################################################
class PlcOutputCountLogView(LoginRequiredMixin,ListView):
    
    template_name = 'monitoring/plc_output_count_log.html'
    model = Plc_Output_Count_Log
    paginate_by = 1

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = 'PLC出力監視'
        ctx['msg'] = 'PLC出力回数の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Plc_Output_Count_Log.objects.select_related('Machine_model').filter(\
                    Q(Machine_model__Customer_machine_id__contains=q_word)|Q(Machine_model__Customer_machine_id__icontains=q_word)|\
                        Q(Machine_model__Machine_model__Machine_model__contains=q_word)|Q(Machine_model__Machine_model__Machine_model__icontains=q_word))
        elif q_date:
            object_list = Plc_Output_Count_Log.objects.select_related('Machine_model').filter(Q(Plc_count_log_input_date__icontains=q_date)|\
                Q(Plc_count_log_input_date__icontains=q_date))
        else:
            object_list = Plc_Output_Count_Log.objects.select_related('Machine_model').order_by('-Plc_count_log_input_date')


        return object_list
################################################################################
class PlcOutputCountLogCreateView(CreateView):
    

    template_name = 'monitoring/plc_output_count_log_create.html'
    model = Plc_Output_Count_Log
    form_class = PlcOutputCountLogCreateForm
    
    success_url = reverse_lazy("main_app:plc_output_count_log") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'PLC出力監視'
        ctx['msg'] = 'PLC出力回数の登録が出来ます。'
        return ctx
    
################################################################################
class PlcOutputCountLogUpdateView(UpdateView):

    template_name = 'monitoring/plc_output_count_log_update.html'
    model = Plc_Output_Count_Log
    form_class = PlcOutputCountLogUpdateForm
    
    success_url = reverse_lazy("main_app:plc_output_count_log") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'PLC出力監視'
        ctx['msg'] = 'PLC出力回数の変更が出来ます。'
        return ctx

################################################################################
class PlcOutputCountLogDeleteView(DeleteView):
    

    template_name = 'monitoring/plc_output_count_log_delete.html'
    model = Plc_Output_Count_Log
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:plc_output_count_log") 
 
