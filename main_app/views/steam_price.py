from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Unit_Price_Steam
from ..forms import SteamPriceCreateForm,SteamPriceUpdateForm
from django.db .models import Q




################################################################################
class SteamPriceView(ListView):
    
    template_name = 'unit_price/steam_price.html'
    model = Unit_Price_Steam
    paginate_by = 10

    
    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['title'] = '蒸気単価'
        ctx['msg'] = '蒸気単価設定の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            try:
                object_list = Unit_Price_Steam.objects.filter(Unit_price_steam=q_word)
            except:    
                object_list = Unit_Price_Steam.objects.filter(Q(Unit_price_steam_memo__contains=q_word)|Q(Unit_price_steam_memo__icontains=q_word))
        elif q_date:
            object_list = Unit_Price_Steam.objects.filter(Unit_price_steam_input_date=q_date)
        else:
            object_list = Unit_Price_Steam.objects.order_by('-Unit_price_steam_input_date')


        return object_list
################################################################################
class SteamPriceCreateView(CreateView):
    

    template_name = 'unit_price/steam_price_create.html'
    model = Unit_Price_Steam
    form_class = SteamPriceCreateForm
    
    success_url = reverse_lazy("main_app:steam_price")

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '蒸気単価'
        ctx['msg'] = '蒸気単価の登録が出来ます。'
        return ctx
    
################################################################################
class SteamPriceUpdateView(UpdateView):

    template_name = 'unit_price/steam_price_update.html'
    model = Unit_Price_Steam
    form_class = SteamPriceUpdateForm
    
    success_url = reverse_lazy("main_app:steam_price")
    
    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '蒸気単価'
        ctx['msg'] = '蒸気単価設定の変更が出来ます。'
        return ctx

################################################################################
class SteamPriceDeleteView(DeleteView):
    

    template_name = 'unit_price/steam_price_delete.html'
    model = Unit_Price_Steam
    #form_class = ElectricPriceCreateForm

    success_url = reverse_lazy("main_app:steam_price")    
         
  
