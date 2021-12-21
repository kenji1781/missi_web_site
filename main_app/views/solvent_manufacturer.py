from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent_Manufacturer,Solvent_Name
from ..forms import SolventManufacturerCreateForm,SolventManufacturerUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class SolventManufacturerView(ListView):
    
    template_name = 'user_conf/solvent_manufacturer.html'
    model = Solvent_Manufacturer
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤メーカー'
        ctx['msg'] = '溶剤メーカー登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Solvent_Manufacturer.objects.filter(Solvent_manu__icontains=q_word)
        
            object_list = Solvent_Manufacturer.objects.filter(Solvent_name__Solvent_name=q_word)
        elif q_date:
            object_list = Solvent_Manufacturer.objects.filter(Solvent_manu_input_date__icontains=q_date)
        else:
            object_list = Solvent_Manufacturer.objects.order_by('-Solvent_manu_input_date')


        return object_list
################################################################################
class SolventManufacturerCreateView(CreateView):
    

    template_name = 'user_conf/solvent_manufacturer_create.html'
    model = Solvent_Manufacturer
    form_class = SolventManufacturerCreateForm
    
    success_url = reverse_lazy("main_app:solvent_manufacturer") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤メーカー'
        ctx['msg'] = '溶剤メーカーの登録が出来ます。'
        return ctx
    
################################################################################
class SolventManufacturerUpdateView(UpdateView):

    template_name = 'user_conf/solvent_manufacturer_update.html'
    model = Solvent_Manufacturer
    form_class = SolventManufacturerUpdateForm
    
    success_url = reverse_lazy("main_app:solvent_manufacturer") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤メーカー'
        ctx['msg'] = '溶剤メーカー登録の変更が出来ます。'
        return ctx

################################################################################
class SolventManufacturerDeleteView(DeleteView):
    

    template_name = 'user_conf/solvent_manufacturer_delete.html'
    model = Solvent_Manufacturer
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:solvent_manufacturer") 
 
