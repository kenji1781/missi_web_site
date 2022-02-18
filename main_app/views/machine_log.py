from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Log
from ..forms import MachineLogCreateForm,MachineLogUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


################################################################################
class MachineLogView(LoginRequiredMixin,ListView):
    
    template_name = 'monitoring/machine_log.html'
    model = Machine_Log
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '稼働時間・回数'
        ctx['msg'] = '稼働時間・回数の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Machine_Log.objects.select_related('Machine_model').filter(\
                    Q(Machine_model__Customer_machine_id__contains=q_word)|Q(Machine_model__Customer_machine_id__icontains=q_word)|\
                        Q(Machine_model__Machine_model__Machine_model__contains=q_word)|Q(Machine_model__Machine_model__Machine_model__icontains=q_word))
        elif q_date:
            object_list = Machine_Log.objects.select_related('Machine_model').filter(Q(Machine_log_input_date__icontains=q_date)|\
                Q(Machine_log_input_date__icontains=q_date))
        else:
            object_list = Machine_Log.objects.select_related('Machine_model').order_by('-Machine_log_input_date')


        return object_list
################################################################################
class MachineLogCreateView(CreateView):
    

    template_name = 'monitoring/machine_log_create.html'
    model = Machine_Log
    form_class = MachineLogCreateForm
    
    success_url = reverse_lazy("main_app:machine_log") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '稼働時間・回数'
        ctx['msg'] = '稼働時間・回数の登録が出来ます。'
        return ctx
    
################################################################################
class MachineLogUpdateView(UpdateView):

    template_name = 'monitoring/machine_log_update.html'
    model = Machine_Log
    form_class = MachineLogUpdateForm
    
    success_url = reverse_lazy("main_app:machine_log") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '稼働時間・回数'
        ctx['msg'] = '稼働時間・回数の変更が出来ます。'
        return ctx

################################################################################
class MachineLogDeleteView(DeleteView):
    

    template_name = 'monitoring/machine_log_delete.html'
    model = Machine_Log
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:machine_log") 
 
