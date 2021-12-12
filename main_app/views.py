from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .models import Unit_Price_Electric,Unit_Price_Electric


class IndexView(TemplateView):
    template_name = 'index.html'



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
################################################################################
class ElectricPriceCreateView(CreateView):
    

    template_name = 'unit_price/electric_price_create.html'
    model = Unit_Price_Electric
    fields = ('Unit_price_electric','Unit_price_electric_input_date','Unit_price_electric_memo')
    success_url = '/electricity_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '電力単価'
        ctx['msg'] = '電力単価設定の確認／変更が出来ます。'
        return ctx
