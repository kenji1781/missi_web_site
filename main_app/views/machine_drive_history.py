from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Drive_History
from ..forms import MachineDriveHistoryCreateForm,MachineDriveHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages
from datetime import datetime,date,time
from ..machine_drive_history_model_comp import ModelComplement
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.utils.timezone import localdate,localtime



################################################################################
class MachineDriveHistoryView(LoginRequiredMixin,ListView):
    
    template_name = 'monitoring/machine_drive_history.html'
    model = Machine_Drive_History
    paginate_by = 50
    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = 'ユーティリティ'
        ctx['msg'] = 'ユーティリティ監視履歴の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Machine_Drive_History.objects.select_related('Customer_machine_recipe').filter(\
                    Q(Customer_machine_recipe__Machine_model__Customer_machine_id__contains=q_word)|Q(Customer_Machine_recipe__Machine_model__Customer_machine_id__icontains=q_word)|\
                        Q(Customer_machine_recipe__Machine_model__Machine_model__contains=q_word)|Q(Customer_Machine_recipe__Machine_model__Machine_model__icontains=q_word))        
       
        elif q_date:
            object_list = Machine_Drive_History.objects.select_related('Customer_machine_recipe').filter(\
                Q(Data_datetime__contains=q_date)|\
                    Q(Data_datetime__icontains=q_date)|\
                        Q(Machine_history_input_date__contains=q_date)|\
                            Q(Machine_history_input_date__icontains=q_date))
                       
        else:
            object_list = Machine_Drive_History.objects.select_related('Customer_machine_recipe').order_by('-Machine_history_input_date')
        
            #稼働履歴モデルの補完を行う##########################
            modelcomp = ModelComplement()
            #datetimeをdateとtimeに分割
            modelcomp.datetime_complement(object_list)
            #idから機種を書込み
            #modelcomp.machine_model_complement(object_list)
            #品種No.から品種名を書込み
            #modelcomp.recipe_model_complement(object_list)
            
            #各最新単価を書込み
            modelcomp.unit_cost_complement(object_list)
            #################################################

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
        ctx['title'] = 'ユーティリティ'
        ctx['msg'] = 'ユーティリティ監視履歴の登録が出来ます。'
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
        ctx['title'] = 'ユーティリティ'
        ctx['msg'] = 'ユーティリティ監視履歴の変更が出来ます。'
        return ctx

################################################################################
class MachineDriveHistoryDeleteView(DeleteView):
    

    template_name = 'monitoring/machine_drive_history_delete.html'
    model = Machine_Drive_History
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:machine_drive_history")
 
