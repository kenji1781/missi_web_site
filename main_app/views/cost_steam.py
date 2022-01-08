from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Drive_History,Cost_Steam,Unit_Price_Steam
from ..forms import CostSteamCreateForm,CostSteamUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class CostSteamView(ListView):
    
    template_name = 'monitoring/cost_steam.html'
    model = Cost_Steam
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '蒸気コスト'
        ctx['msg'] = '蒸気コスト確認が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Cost_Steam.objects.select_related('Machine_model').filter(\
                Q(Machine_drive_history__Machine_model__contains=q_word)|Q(Machine_drive_history__Machine_model__icontains=q_word))
            #object_list = Solvent_Conf.objects.select_related().filter(Solvent_manu__Solvent_manu=q_word)
            
            #object_list = Solvent_Conf.objects.filter(Solvent_memo__icontains=q_word)
        elif q_date:
            object_list = Cost_Steam.objects.filter(Data_datetime__icontains=q_date)
        else:
            object_list = Cost_Steam.objects.select_related('Machine_model').order_by('-Machine_model_input_date')


        return object_list
################################################################################
class CostSteamCreateView(CreateView):
    

    template_name = 'monitoring/cost_steam_create.html'
    model = Cost_Steam
    form_class = CostSteamCreateForm
    
    success_url = reverse_lazy("main_app:cost_steam") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '蒸気コスト'
        ctx['msg'] = '蒸気コストの登録が出来ます。'
        return ctx
    
################################################################################
class CostSteamUpdateView(UpdateView):

    template_name = 'monitoring/cost_steam_update.html'
    model = Cost_Steam
    form_class = CostSteamUpdateForm
    
    success_url = reverse_lazy("main_app:cost_steam") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '蒸気コスト'
        ctx['msg'] = '蒸気コスト登録の変更が出来ます。'
        return ctx

################################################################################
class CostSteamDeleteView(DeleteView):
    

    template_name = 'monitoring/cost_steam_delete.html'
    model = Cost_Steam
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:cost_steam") 
 
