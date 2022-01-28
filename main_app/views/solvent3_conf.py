from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent3_Conf
from ..forms import Solvent3ConfCreateForm,Solvent3ConfUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


################################################################################
class Solvent3ConfView(LoginRequiredMixin,ListView):
    
    template_name = 'unit_price/solvent3_conf.html'
    model = Solvent3_Conf
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤3単価'
        ctx['msg'] = '溶剤3単価登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            try:
                object_list = Solvent3_Conf.objects.filter(Unit_price_solvent3=q_word)
                
            except:
                object_list = Solvent3_Conf.objects.select_related('Solvent3_name','Solvent3_manu').filter(\
                    Q(Solvent3_memo__contains=q_word)|Q(Solvent3_memo__icontains=q_word)|\
                        Q(Solvent3_name__Solvent_name__contains=q_word)|Q(Solvent3_name__Solvent_name__icontains=q_word)|\
                            Q(Solvent3_manu__Solvent_manu__contains=q_word)|Q(Solvent3_manu__Solvent_manu__icontains=q_word))


            #object_list = Solvent_Conf.objects.select_related().filter(Solvent_manu__Solvent_manu=q_word)
            
            #object_list = Solvent_Conf.objects.filter(Solvent_memo__icontains=q_word)
        elif q_date:
            object_list = Solvent3_Conf.objects.filter(Solvent3_input_date__icontains=q_date)
        else:
            object_list = Solvent3_Conf.objects.select_related('Solvent3_name','Solvent3_manu').order_by('-Solvent3_input_date')


        return object_list
################################################################################
class Solvent3ConfCreateView(CreateView):
    

    template_name = 'unit_price/solvent3_conf_create.html'
    model = Solvent3_Conf
    form_class = Solvent3ConfCreateForm
    
    success_url = reverse_lazy("main_app:solvent3_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤3単価'
        ctx['msg'] = '溶剤3単価の登録が出来ます。'
        return ctx
    
################################################################################
class Solvent3ConfUpdateView(UpdateView):

    template_name = 'unit_price/solvent3_conf_update.html'
    model = Solvent3_Conf
    form_class = Solvent3ConfUpdateForm
    
    success_url = reverse_lazy("main_app:solvent3_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤3単価'
        ctx['msg'] = '溶剤3単価登録の変更が出来ます。'
        return ctx

################################################################################
class Solvent3ConfDeleteView(DeleteView):
    

    template_name = 'unit_price/solvent3_conf_delete.html'
    model = Solvent3_Conf
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:solvent3_conf") 
 
