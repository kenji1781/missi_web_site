from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Maintenance_Mail_Setting
from ..forms import MaintenanceEmailCreateForm,MaintenanceEmailUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class MaintenanceEmailView(LoginRequiredMixin,ListView):
    
    template_name = 'user_conf/maintenance_email.html'
    model = Maintenance_Mail_Setting
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = 'メール通知設定'
        ctx['msg'] = 'メール通知登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Maintenance_Mail_Setting.objects.select_related('Maintenance_machine_history','Maintenance_mail_notification').filter(\
                    Q(Maintenance_threshold__contains=q_word)|Q(Maintenance_threshold__icontains=q_word)|\
                        Q(Maintenance_send_setting__contains=q_word)|Q(Maintenance_send_setting__icontains=q_word)|\
                            Q(Maintenance_memo__contains=q_word)|Q(Maintenance_memo__icontains=q_word)|\
                                Q(Maintenance_machine_history__Machine_model__contains=q_word)|Q(Maintenance_machine_history__Machine_model__icontains=q_word)|\
                                    Q(Maintenance_mail_notification__Mail_name__contains=q_word)|Q(Maintenance_mail_notification__Mail_name__icontains=q_word)|\
                                        Q(Maintenance_mail_notification__Mail_address__contains=q_word)|Q(Maintenance_mail_notification__Mail_address__icontains=q_word))
        elif q_date:
            object_list = Maintenance_Mail_Setting.objects.select_related('Maintenance_machine_history','Maintenance_mail_notification').filter(Q(Maintenance_input_date__icontains=q_date)|\
                Q(Maintenance_input_date__icontains=q_date))
        else:
            object_list = Maintenance_Mail_Setting.objects.select_related('Maintenance_machine_history','Maintenance_mail_notification').order_by('-Maintenance_input_date')


        return object_list
################################################################################
class MaintenanceEmailCreateView(CreateView):
    

    template_name = 'user_conf/maintenance_email_create.html'
    model = Maintenance_Mail_Setting
    form_class = MaintenanceEmailCreateForm
    
    success_url = reverse_lazy("main_app:maintenance_email") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'メール通知設定'
        ctx['msg'] = 'メール通知設定の登録が出来ます。'
        return ctx
    
################################################################################
class MaintenanceEmailUpdateView(UpdateView):

    template_name = 'user_conf/maintenance_email_update.html'
    model = Maintenance_Mail_Setting
    form_class = MaintenanceEmailUpdateForm
    
    success_url = reverse_lazy("main_app:maintenance_email") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'メール通知設定'
        ctx['msg'] = 'メール通知設定登録の変更が出来ます。'
        return ctx

################################################################################
class MaintenanceEmailDeleteView(DeleteView):
    

    template_name = 'user_conf/maintenance_email_delete.html'
    model = Maintenance_Mail_Setting
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:maintenance_email") 
 
