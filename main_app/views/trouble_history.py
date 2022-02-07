from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Trouble_History
from ..forms import TroubleHistoryCreateForm,TroubleHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages
from datetime import datetime,date,time
from ..trouble_history_model_comp import ModelComplement
from django.contrib.auth.mixins import LoginRequiredMixin

################################################################################
class TroubleHistoryView(LoginRequiredMixin,ListView):
    
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
            object_list = Trouble_History.objects.select_related('Trouble_contents')\
                .filter(Q(Trouble_contents__Trouble_no__contains=q_word)|Q(Trouble_contents__Trouble_no__icontains=q_word)|\
                            Q(Trouble_contents__Trouble_contents__contains=q_word)|Q(Trouble_contents__Trouble_contents__icontains=q_word)|\
                                Q(Trouble_contents__Trouble_memo__contains=q_word)|Q(Trouble_contents__Trouble_memo__icontains=q_word))\
                .filter(Trouble_occurrence_time__range=(q_date_f, q_date_l))
                
            
        else:
            object_list = Trouble_History.objects.select_related('Trouble_contents').all().order_by('-Trouble_occurrence_time')    #.values('Customer_machine_id','Machine_model','Customer_machine_unit_no','Cost_electric','Data_datetime')

            modelcomp = ModelComplement()
            #装置IDから客先装置型式号機　ロスタイムを補完
            modelcomp.trouble_history_model_complement(object_list)
            
        
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
 
