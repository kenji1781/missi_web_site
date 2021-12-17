from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Unit_Price_Water
from ..forms import WaterPriceCreateForm,WaterPriceUpdateForm
from django.db .models import Q




################################################################################
class WaterPriceView(ListView):
    
    template_name = 'unit_price/water_price.html'
    model = Unit_Price_Water
    paginate_by = 10

    
    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['title'] = '水単価'
        ctx['msg'] = '水単価設定の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Unit_Price_Water.objects.filter(Q(Unit_price_water__icontains=q_word)|Q(Unit_price_water_memo=q_word))
        elif q_date:
            object_list = Unit_Price_Water.objects.filter(Q(Unit_price_water_input_date__icontains=q_date))
        else:
            object_list = Unit_Price_Water.objects.order_by('-Unit_price_water_input_date')


        return object_list
################################################################################
class WaterPriceCreateView(CreateView):
    

    template_name = 'unit_price/water_price_create.html'
    model = Unit_Price_Water
    form_class = WaterPriceCreateForm
    
    success_url = '/water_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '水単価'
        ctx['msg'] = '水単価の登録が出来ます。'
        return ctx
    
################################################################################
class WaterPriceUpdateView(UpdateView):

    template_name = 'unit_price/water_price_update.html'
    model = Unit_Price_Water
    form_class = WaterPriceUpdateForm
    
    success_url = '/water_unit_price/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '水単価'
        ctx['msg'] = '水単価設定の変更が出来ます。'
        return ctx

################################################################################
class WaterPriceDeleteView(DeleteView):
    

    template_name = 'unit_price/water_price_delete.html'
    model = Unit_Price_Water
    #form_class = ElectricPriceCreateForm
    
    success_url = '/water_unit_price/'    #reverse_lazy("electric_price")     
  
