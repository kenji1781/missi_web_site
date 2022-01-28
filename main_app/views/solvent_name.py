from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent_Name
from ..forms import SolventNameCreateForm,SolventNameUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


################################################################################
class SolventNameView(LoginRequiredMixin,ListView):
    
    template_name = 'user_conf/solvent_name.html'
    model = Solvent_Name
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '溶剤名'
        ctx['msg'] = '溶剤名の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Solvent_Name.objects.filter(Q(Solvent_name__contains=q_word)|Q(Solvent_name__icontains=q_word))
        elif q_date:
            object_list = Solvent_Name.objects.filter(Solvent_name_input_date=q_date)
        else:
            object_list = Solvent_Name.objects.order_by('-Solvent_name_input_date')


        return object_list
################################################################################
class SolventNameCreateView(CreateView):
    

    template_name = 'user_conf/solvent_name_create.html'
    model = Solvent_Name
    form_class = SolventNameCreateForm
    
    success_url = reverse_lazy("main_app:solvent_name") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤名'
        ctx['msg'] = '溶剤名の登録が出来ます。'
        return ctx
    
################################################################################
class SolventNameUpdateView(UpdateView):

    template_name = 'user_conf/solvent_name_update.html'
    model = Solvent_Name
    form_class = SolventNameUpdateForm
    
    success_url = reverse_lazy("main_app:solvent_name") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '溶剤名'
        ctx['msg'] = '溶剤名の変更が出来ます。'
        return ctx

################################################################################
class SolventNameDeleteView(DeleteView):
    

    template_name = 'user_conf/solvent_name_delete.html'
    model = Solvent_Name
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:solvent_name") 
 
