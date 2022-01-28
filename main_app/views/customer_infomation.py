from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Infomation
from ..forms import CustomerInfomationCreateForm,CustomerInfomationUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class CustomerInfomationView(LoginRequiredMixin,ListView):
    
    template_name = 'manufacturer_setting/customer_infomation.html'
    model = Customer_Infomation
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '客先情報'
        ctx['msg'] = '客先情報登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Customer_Infomation.objects.filter(\
                    Q(Customer_name__contains=q_word)|Q(Customer_name__icontains=q_word)|\
                        Q(Customer_tel_number__contains=q_word)|Q(Customer_tel_number__icontains=q_word)|\
                            Q(Customer_pastal_code__contains=q_word)|Q(Customer_pastal_code__icontains=q_word)|\
                                Q(Customer_address1__contains=q_word)|Q(Customer_address1__icontains=q_word)|\
                                    Q(Customer_address2__contains=q_word)|Q(Customer_address2__icontains=q_word)|\
                                        Q(Customer_address3__contains=q_word)|Q(Customer_address3__icontains=q_word)|\
                                            Q(Customer_memo__contains=q_word)|Q(Customer_memo__icontains=q_word))
        elif q_date:
            object_list = Customer_Infomation.objects.filter(Q(Customer_input_date__contains=q_date)|\
                Q(Customer_input_date__icontains=q_date))
        else:
            object_list = Customer_Infomation.objects.order_by('-Customer_input_date')


        return object_list
################################################################################
class CustomerInfomationCreateView(CreateView):
    

    template_name = 'manufacturer_setting/customer_infomation_create.html'
    model = Customer_Infomation
    form_class = CustomerInfomationCreateForm
    
    success_url = reverse_lazy("main_app:customer_infomation") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '客先情報'
        ctx['msg'] = '客先情報の登録が出来ます。'
        return ctx
    
################################################################################
class CustomerInfomationUpdateView(UpdateView):

    template_name = 'manufacturer_setting/customer_infomation_update.html'
    model = Customer_Infomation
    form_class = CustomerInfomationUpdateForm
    
    success_url = reverse_lazy("main_app:customer_infomation") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '客先情報'
        ctx['msg'] = '客先情報登録の変更が出来ます。'
        return ctx

################################################################################
class CustomerInfomationDeleteView(DeleteView):
    

    template_name = 'manufacturer_setting/customer_infomation_delete.html'
    model = Customer_Infomation
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:customer_infomation") 
 
