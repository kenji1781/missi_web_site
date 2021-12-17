from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Unit_Price_Gas
from ..forms import GasPriceCreateForm,GasPriceUpdateForm
from django.db .models import Q




################################################################################
class GasPriceView(ListView):
    
    template_name = 'unit_price/gas_price.html'
    model = Unit_Price_Gas
    paginate_by = 10

    
    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['title'] = 'ガス単価'
        ctx['msg'] = 'ガス単価設定の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Unit_Price_Gas.objects.filter(Q(Unit_price_gas__icontains=q_word)|Q(Unit_price_gas_memo=q_word))
        elif q_date:
            object_list = Unit_Price_Gas.objects.filter(Q(Unit_price_gas_input_date__icontains=q_date))
        else:
            object_list = Unit_Price_Gas.objects.order_by('-Unit_price_gas_input_date')


        return object_list
################################################################################
class GasPriceCreateView(CreateView):
    

    template_name = 'unit_price/gas_price_create.html'
    model = Unit_Price_Gas
    form_class = GasPriceCreateForm
    
    success_url = '/gas_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = 'ガス単価'
        ctx['msg'] = 'ガス単価の登録が出来ます。'
        return ctx
    
################################################################################
class GasPriceUpdateView(UpdateView):

    template_name = 'unit_price/gas_price_update.html'
    model = Unit_Price_Gas
    form_class = GasPriceUpdateForm
    
    success_url = '/gas_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = 'ガス単価'
        ctx['msg'] = 'ガス単価設定の変更が出来ます。'
        return ctx

################################################################################
class GasPriceDeleteView(DeleteView):
    

    template_name = 'unit_price/gas_price_delete.html'
    model = Unit_Price_Gas
    #form_class = ElectricPriceCreateForm
    
    success_url = '/gas_unit_price/'    #reverse_lazy("electric_price")     
  
