from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Mail_Notification
from ..forms import MailNotificationCreateForm,MailNotificationUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class MailNotificationView(LoginRequiredMixin,ListView):
    
    template_name = 'user_conf/mail_notification.html'
    model = Mail_Notification
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = 'メール登録'
        ctx['msg'] = 'メール登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Mail_Notification.objects.filter(\
                    Q(Mail_name__contains=q_word)|Q(Mail_name__icontains=q_word)|\
                        Q(Mail_department__contains=q_word)|Q(Mail_department__icontains=q_word)|\
                            Q(Mail_address__contains=q_word)|Q(Mail_address__icontains=q_word)|\
                                Q(Mail_memo__contains=q_word)|Q(Mail_memo__icontains=q_word))
        elif q_date:
            object_list = Mail_Notification.objects.filter(Q(Mail_input_date__icontains=q_date)|\
                Q(Mail_input_date__icontains=q_date))
        else:
            object_list = Mail_Notification.objects.order_by('-Mail_input_date')


        return object_list
################################################################################
class MailNotificationCreateView(CreateView):
    

    template_name = 'user_conf/mail_notification_create.html'
    model = Mail_Notification
    form_class = MailNotificationCreateForm
    
    success_url = reverse_lazy("main_app:mail_notification") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'メール登録'
        ctx['msg'] = 'メール登録が出来ます。'
        return ctx
    
################################################################################
class MailNotificationUpdateView(UpdateView):

    template_name = 'user_conf/mail_notification_update.html'
    model = Mail_Notification
    form_class = MailNotificationUpdateForm
    
    success_url = reverse_lazy("main_app:mail_notification") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'メール登録'
        ctx['msg'] = 'メール登録の変更が出来ます。'
        return ctx

################################################################################
class MailNotificationDeleteView(DeleteView):
    

    template_name = 'user_conf/mail_notification_delete.html'
    model = Mail_Notification
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:mail_notification") 
 
