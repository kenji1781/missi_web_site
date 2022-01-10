from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent1_Conf
from ..forms import Solvent1ConfCreateForm,Solvent1ConfUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class Solvent1ConfView(ListView):
    
    template_name = 'unit_price/solvent1_conf.html'
    model = Solvent1_Conf
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤1単価'
        ctx['msg'] = '溶剤1単価登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            try:
                object_list = Solvent1_Conf.objects.filter(Unit_price_solvent1=q_word)
                
            except:
                object_list = Solvent1_Conf.objects.select_related('Solvent1_name','Solvent1_manu').filter(\
                    Q(Solvent1_memo__contains=q_word)|Q(Solvent1_memo__icontains=q_word)|\
                        Q(Solvent1_name__Solvent_name__contains=q_word)|Q(Solvent1_name__Solvent_name__icontains=q_word)|\
                            Q(Solvent1_manu__Solvent_manu__contains=q_word)|Q(Solvent1_manu__Solvent_manu__icontains=q_word))


            #object_list = Solvent_Conf.objects.select_related().filter(Solvent_manu__Solvent_manu=q_word)
            
            #object_list = Solvent_Conf.objects.filter(Solvent_memo__icontains=q_word)
        elif q_date:
            object_list = Solvent1_Conf.objects.filter(Solvent1_input_date__icontains=q_date)
        else:
            object_list = Solvent1_Conf.objects.select_related('Solvent1_name','Solvent1_manu').order_by('-Solvent1_input_date')


        return object_list
################################################################################
class Solvent1ConfCreateView(CreateView):
    

    template_name = 'unit_price/solvent1_conf_create.html'
    model = Solvent1_Conf
    form_class = Solvent1ConfCreateForm
    
    success_url = reverse_lazy("main_app:solvent1_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤1単価'
        ctx['msg'] = '溶剤1単価の登録が出来ます。'
        return ctx
    
################################################################################
class Solvent1ConfUpdateView(UpdateView):

    template_name = 'unit_price/solvent1_conf_update.html'
    model = Solvent1_Conf
    form_class = Solvent1ConfUpdateForm
    
    success_url = reverse_lazy("main_app:solvent1_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤1単価'
        ctx['msg'] = '溶剤1単価登録の変更が出来ます。'
        return ctx

################################################################################
class Solvent1ConfDeleteView(DeleteView):
    

    template_name = 'unit_price/solvent1_conf_delete.html'
    model = Solvent1_Conf
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:solvent1_conf") 
 
