from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Machine
from ..forms import CustomerMachineCreateForm,CustomerMachineUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class CustomerMachineView(ListView):
    
    template_name = 'user_conf/customer_machine.html'
    model = Customer_Machine
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '装置設定'
        ctx['msg'] = 'ユーザー装置登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Customer_Machine.objects.select_related('Machine_model').filter(\
                    Q(Customer_machine_id__contains=q_word)|Q(Customer_machine_id__icontains=q_word)|\
                        Q(Customer_machine_unit_no__contains=q_word)|Q(Customer_machine_unit_no__icontains=q_word)|\
                            Q(Customer_machine_memo__contains=q_word)|Q(Customer_machine_memo__icontains=q_word)|\
                                Q(Machine_model__Machine_model__contains=q_word)|Q(Machine_model__Machine_model__icontains=q_word))
        elif q_date:
            object_list = Customer_Machine.objects.select_related('Machine_model').filter(Q(Customer_machine_inst_date__icontains=q_date)|\
                Q(Customer_machine_input_date__icontains=q_date))
        else:
            object_list = Customer_Machine.objects.select_related('Machine_model').order_by('-Customer_machine_input_date')


        return object_list
################################################################################
class CustomerMachineCreateView(CreateView):
    

    template_name = 'user_conf/customer_machine_create.html'
    model = Customer_Machine
    form_class = CustomerMachineCreateForm
    
    success_url = reverse_lazy("main_app:customer_machine") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '装置設定'
        ctx['msg'] = 'ユーザー装置の登録が出来ます。'
        return ctx
    
################################################################################
class CustomerMachineUpdateView(UpdateView):

    template_name = 'user_conf/customer_machine_update.html'
    model = Customer_Machine
    form_class = CustomerMachineUpdateForm
    
    success_url = reverse_lazy("main_app:customer_machine") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '装置設定'
        ctx['msg'] = 'ユーザー装置登録の変更が出来ます。'
        return ctx

################################################################################
class CustomerMachineDeleteView(DeleteView):
    

    template_name = 'user_conf/customer_machine_delete.html'
    model = Customer_Machine
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:customer_machine") 
 
