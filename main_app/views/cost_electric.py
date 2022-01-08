from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Cost_Electric,Unit_Price_Electric,Machine_Drive_History
from ..forms import CostElectricCreateForm,CostElectricUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class CostElectricView(ListView):
    
    template_name = 'monitoring/cost_electric.html'
    model = Cost_Electric
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '電力コスト'
        ctx['msg'] = '電力コスト確認が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date_f = self.request.GET.get('query_date_f')
        q_date_l = self.request.GET.get('query_date_l')
        if q_word and q_date_f and q_date_l:
            object_list = Cost_Electric.objects.filter(\
                Q(Machine_drive_history__Machine_model__contains=q_word)|Q(Machine_drive_history__Machine_model__icontains=q_word))
        else:
            object_list = Cost_Electric.objects.select_related('Machine_drive_history','Unit_price_electric').order_by('-Data_datetime')
            

        return object_list
################################################################################
class CostElectricCreateView(CreateView):
    

    template_name = 'monitoring/cost_electric_create.html'
    model = Cost_Electric
    form_class = CostElectricCreateForm
    
    success_url = reverse_lazy("main_app:cost_electric") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '電力コスト'
        ctx['msg'] = '電力コストの登録が出来ます。'
        return ctx
    
################################################################################
class CostElectricUpdateView(UpdateView):

    template_name = 'monitoring/cost_electric_update.html'
    model = Cost_Electric
    form_class = CostElectricUpdateForm
    
    success_url = reverse_lazy("main_app:cost_electric") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '電力コスト'
        ctx['msg'] = '電力コスト登録の変更が出来ます。'
        return ctx

################################################################################
class CostElectricDeleteView(DeleteView):
    

    template_name = 'monitoring/cost_electric_delete.html'
    model = Cost_Electric
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:cost_electric") 
 
