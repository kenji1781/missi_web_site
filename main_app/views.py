from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .models import Unit_Price_Electric


class IndexView(TemplateView):
    template_name = 'index.html'
index = IndexView.as_view()


class ElectricPriceView(ListView):
    def __init__(self):
        self.params = {
            'title' : "電力単価",
            'msg' : "電力単価設定の確認/変更が出来ます。"
        }
    def get(self,request):
        return render(request,'unit_price/electric_price.html',self.params)

    template_name = 'unit/priceelectric_price.html'
    model = Unit_Price_Electric

electric_price = ElectricPriceView.as_view()



"""
def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう１つのページです。',
        'goto':'index',
    }
    return render(request, 'index.html', params)
"""