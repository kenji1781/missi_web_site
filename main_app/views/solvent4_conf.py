from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent4_Conf
from ..forms import Solvent4ConfCreateForm,Solvent4ConfUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


################################################################################
class Solvent4ConfView(LoginRequiredMixin,ListView):
    
    template_name = 'unit_price/solvent4_conf.html'
    model = Solvent4_Conf
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤4単価'
        ctx['msg'] = '溶剤4単価登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            try:
                object_list = Solvent4_Conf.objects.filter(Unit_price_solvent4=q_word)
                
            except:
                object_list = Solvent4_Conf.objects.select_related('Solvent4_name','Solvent4_manu').filter(\
                    Q(Solvent4_memo__contains=q_word)|Q(Solvent4_memo__icontains=q_word)|\
                        Q(Solvent4_name__Solvent_name__contains=q_word)|Q(Solvent4_name__Solvent_name__icontains=q_word)|\
                            Q(Solvent4_manu__Solvent_manu__contains=q_word)|Q(Solvent4_manu__Solvent_manu__icontains=q_word))


            #object_list = Solvent_Conf.objects.select_related().filter(Solvent_manu__Solvent_manu=q_word)
            
            #object_list = Solvent_Conf.objects.filter(Solvent_memo__icontains=q_word)
        elif q_date:
            object_list = Solvent4_Conf.objects.filter(Solvent4_input_date__icontains=q_date)
        else:
            object_list = Solvent4_Conf.objects.select_related('Solvent4_name','Solvent4_manu').order_by('-Solvent4_input_date')


        return object_list
################################################################################
class Solvent4ConfCreateView(CreateView):
    

    template_name = 'unit_price/solvent4_conf_create.html'
    model = Solvent4_Conf
    form_class = Solvent4ConfCreateForm
    
    success_url = reverse_lazy("main_app:solvent4_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤4単価'
        ctx['msg'] = '溶剤4単価の登録が出来ます。'
        return ctx
    
################################################################################
class Solvent4ConfUpdateView(UpdateView):

    template_name = 'unit_price/solvent4_conf_update.html'
    model = Solvent4_Conf
    form_class = Solvent4ConfUpdateForm
    
    success_url = reverse_lazy("main_app:solvent4_conf") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤4単価'
        ctx['msg'] = '溶剤4単価登録の変更が出来ます。'
        return ctx

################################################################################
class Solvent4ConfDeleteView(DeleteView):
    

    template_name = 'unit_price/solvent4_conf_delete.html'
    model = Solvent4_Conf
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:solvent4_conf") 
 
