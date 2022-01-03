from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Machine_Recipe,Customer_Machine,Machine_Drive_History
from ..forms import MachineDriveHistoryCreateForm,MachineDriveHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class MachineDriveHistoryView(ListView):
    
    template_name = 'monitoring/machine_drive_history.html'
    model = Machine_Drive_History
    paginate_by = 10

    for history_i in Machine_Drive_History.objects.all():
        for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
            if (history_i.Signal_plc_to_sys == True)or\
                    ((history_i.Machine_model==None) and (history_i.Customer_machine_id != None))or\
                        ((history_i.Customer_machine_id == c_machine.Customer_machine_id)and(history_i.Machine_model != c_machine.Machine_model)):
                for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                    if history_i.Customer_machine_id == c_machine.Customer_machine_id:
                        history_i.Machine_model = str(c_machine.Machine_model)+ ': #' +str(c_machine.Customer_machine_unit_no)                   
                                               
                                        
            history_i.Signal_plc_to_sys = False
            history_i.save()





    
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
    model = Customer_Machine_Recipe
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:customer_machine_recipe") 
 
