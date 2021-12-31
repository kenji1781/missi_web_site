from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Trouble_History
from ..forms import TroubleHistoryCreateForm,TroubleHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class TroubleHistoryView(ListView):
    
    template_name = 'monitoring/trouble_history.html'
    model = Trouble_History
    paginate_by = 10

    for history in Trouble_History.objects.all():
        if history.Signal_plc_to_sys == True:
            date1 = history.Trouble_recovery_time    
            date2 = history.Trouble_occurrence_time
            loss_time = date1-date2
            print(loss_time)
            history.Trouble_loss_time = loss_time
            #history.save()

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Trouble_History.objects.filter(\
                    Q(Customer_machine_id__contains=q_word)|Q(Customer_machine_id__icontains=q_word)|\
                        Q(Machine_model__contains=q_word)|Q(Machine_model__icontains=q_word)|\
                            Q(Customer_machine_unit_no__contains=q_word)|Q(Customer_machine_unit_no__icontains=q_word)|\
                                Q(Trouble_no__contains=q_word)|Q(Trouble_no__icontains=q_word)|\
                                Q(Trouble_contents__contains=q_word)|Q(Trouble_contents__icontains=q_word))
        elif q_date:
            object_list = Trouble_History.objects.filter(\
                Q(Trouble_occurrence_time__contains=q_date)|\
                    Q(Trouble_occurrence_time__icontains=q_date)|\
                        Q(Trouble_recovery_time__contains=q_date)|\
                            Q(Trouble_recovery_time__icontains=q_date))
        else:
            object_list = Trouble_History.objects.order_by('-Trouble_occurrence_time')


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
 
