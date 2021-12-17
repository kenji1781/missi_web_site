from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Unit_Price_Electric,Unit_Price_Electric
from ..forms import ElectricPriceCreateForm,ElectricPriceUpdateForm
from django.db .models import Q




################################################################################
class ElectricPriceView(ListView):
    
    template_name = 'unit_price/electric_price.html'
    model = Unit_Price_Electric
    
    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['title'] = '電力単価'
        ctx['msg'] = '電力単価設定の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_woed = self.request.GET.get('query')

        if q_woed:
            object_list = Unit_Price_Electric.objects.filter(Q(Unit_price_electric__icontains=q_woed)|Q(Unit_price_electric_memo=q_woed))

        else:
            object_list = Unit_Price_Electric.objects.order_by('-Unit_price_electric_input_date')


        return object_list
################################################################################
class ElectricPriceCreateView(CreateView):
    

    template_name = 'unit_price/electric_price_create.html'
    model = Unit_Price_Electric
    form_class = ElectricPriceCreateForm
    
    success_url = '/electricity_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '電力単価'
        ctx['msg'] = '電力単価の登録が出来ます。'
        return ctx
    
################################################################################
class ElectricPriceUpdateView(UpdateView):

    template_name = 'unit_price/electric_price_update.html'
    model = Unit_Price_Electric
    form_class = ElectricPriceUpdateForm
    
    success_url = '/electricity_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '電力単価'
        ctx['msg'] = '電力単価設定の変更が出来ます。'
        return ctx

################################################################################
class ElectricPriceDeleteView(DeleteView):
    

    template_name = 'unit_price/electric_price_delete.html'
    model = Unit_Price_Electric
    #form_class = ElectricPriceCreateForm
    
    success_url = '/electricity_unit_price/'    #reverse_lazy("electric_price")     
  
