from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Solvent_Name
from ..forms import SolventNameCreateForm,SolventNameUpdateForm
from django.db .models import Q




################################################################################
class SolventNameView(ListView):
    
    template_name = 'unit_price/solvent_name.html'
    model = Solvent_Name
    paginate_by = 10

    
    def get_context_data(self):
        ctx = super().get_context_data()

        # page_title を追加する
        ctx['title'] = '溶剤名'
        ctx['msg'] = '溶剤名の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Solvent_Name.objects.filter(Q(Solvent_name__icontains=q_word))
        elif q_date:
            object_list = Solvent_Name.objects.filter(Q(Solvent_name_input_date__icontains=q_date))
        else:
            object_list = Solvent_Name.objects.order_by('-Solvent_name_input_date')


        return object_list
################################################################################
class SolventNameCreateView(CreateView):
    

    template_name = 'unit_price/solvent_name_create.html'
    model = Solvent_Name
    form_class = SolventNameCreateForm
    
    success_url = '/solvent_name/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '溶剤名'
        ctx['msg'] = '溶剤名の登録が出来ます。'
        return ctx
    
################################################################################
class SolventNameUpdateView(UpdateView):

    template_name = 'unit_price/solvent_name_update.html'
    model = Solvent_Name
    form_class = SolventNameUpdateForm
    
    success_url = '/solvent_name/'    #reverse_lazy("electric_price")     

    def get_context_data(self):
        ctx = super().get_context_data()
        # page_title を追加する
        ctx['title'] = '溶剤名'
        ctx['msg'] = '溶剤名の変更が出来ます。'
        return ctx

################################################################################
class SolventNameDeleteView(DeleteView):
    

    template_name = 'unit_price/solvent_name_delete.html'
    model = Solvent_Name
    #form_class = ElectricPriceCreateForm
    
    success_url = '/solvent_name/'    #reverse_lazy("electric_price")     
  
