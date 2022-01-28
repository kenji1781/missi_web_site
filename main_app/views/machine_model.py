from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Model
from ..forms import MachineModelCreateForm,MachineModelUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class MachineModelView(LoginRequiredMixin,ListView):
    
    template_name = 'manufacturer_setting/machine_model.html'
    model = Machine_Model
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '装置型式'
        ctx['msg'] = '装置型式登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Machine_Model.objects.select_related('Machine_category').filter(\
                Q(Machine_model__contains=q_word)|Q(Machine_model__icontains=q_word)|\
                    Q(Machine_model_memo__contains=q_word)|Q(Machine_model_memo__icontains=q_word)|\
                        Q(Machine_category__Equipment_category__contains=q_word)|Q(Machine_category__Equipment_category__icontains=q_word))
            #object_list = Solvent_Conf.objects.select_related().filter(Solvent_manu__Solvent_manu=q_word)
            
            #object_list = Solvent_Conf.objects.filter(Solvent_memo__icontains=q_word)
        elif q_date:
            object_list = Machine_Model.objects.filter(Machine_model_input_date__icontains=q_date)
        else:
            object_list = Machine_Model.objects.select_related('Machine_category').order_by('-Machine_model_input_date')


        return object_list
################################################################################
class MachineModelCreateView(CreateView):
    

    template_name = 'manufacturer_setting/machine_model_create.html'
    model = Machine_Model
    form_class = MachineModelCreateForm
    
    success_url = reverse_lazy("main_app:machine_model") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '装置型式'
        ctx['msg'] = '装置型式の登録が出来ます。'
        return ctx
    
################################################################################
class MachineModelUpdateView(UpdateView):

    template_name = 'manufacturer_setting/machine_model_update.html'
    model = Machine_Model
    form_class = MachineModelUpdateForm
    
    success_url = reverse_lazy("main_app:machine_model") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '装置型式'
        ctx['msg'] = '装置型式登録の変更が出来ます。'
        return ctx

################################################################################
class MachineModelDeleteView(DeleteView):
    

    template_name = 'manufacturer_setting/machine_model_delete.html'
    model = Machine_Model
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:machine_model") 
 
