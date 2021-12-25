from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent_Conf
from ..forms import SolventConfCreateForm,SolventConfUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class SolventConfView(ListView):
    
    template_name = 'unit_price/solvent_conf.html'
    model = Solvent_Conf
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤単価'
        ctx['msg'] = '溶剤単価登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            try:
                object_list = Solvent_Conf.objects.filter(Solvent_unit_price=q_word)
                
            except:
                object_list = Solvent_Conf.objects.select_related('Solvent_name','Solvent_manu').filter(\
                    Q(Solvent_memo__contains=q_word)|Q(Solvent_memo__icontains=q_word)|\
                        Q(Solvent_name__Solvent_name__contains=q_word)|Q(Solvent_name__Solvent_name__icontains=q_word)|\
                            Q(Solvent_manu__Solvent_manu__contains=q_word)|Q(Solvent_manu__Solvent_manu__icontains=q_word))


            #object_list = Solvent_Conf.objects.select_related().filter(Solvent_manu__Solvent_manu=q_word)
            
            #object_list = Solvent_Conf.objects.filter(Solvent_memo__icontains=q_word)
        elif q_date:
            object_list = Solvent_Conf.objects.filter(Solvent_input_date__icontains=q_date)
        else:
            object_list = Solvent_Conf.objects.select_related('Solvent_name','Solvent_manu').order_by('-Solvent_input_date')


        return object_list
################################################################################
class SolventConfCreateView(CreateView):
    

    template_name = 'unit_price/solvent_conf_create.html'
    model = Solvent_Conf
    form_class = SolventConfCreateForm
    
    success_url = reverse_lazy("main_app:solvent_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤単価'
        ctx['msg'] = '溶剤単価の登録が出来ます。'
        return ctx
    
################################################################################
class SolventConfUpdateView(UpdateView):

    template_name = 'unit_price/solvent_conf_update.html'
    model = Solvent_Conf
    form_class = SolventConfUpdateForm
    
    success_url = reverse_lazy("main_app:solvent_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤単価'
        ctx['msg'] = '溶剤単価登録の変更が出来ます。'
        return ctx

################################################################################
class SolventConfDeleteView(DeleteView):
    

    template_name = 'unit_price/solvent_conf_delete.html'
    model = Solvent_Conf
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:solvent_conf") 
 
