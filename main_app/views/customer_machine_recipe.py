from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Machine_Recipe,Customer_Machine,Trouble_Contents
from ..forms import CustomerMachineRecipeCreateForm,CustomerMachineRecipeUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class CustomerMachineRecipeView(LoginRequiredMixin,ListView):
    
    template_name = 'user_conf/customer_machine_recipe.html'
    model = Customer_Machine_Recipe
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = 'コース設定'
        ctx['msg'] = '装置運転コースの設定確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word_mid = self.request.GET.get('query_text_mid')
        q_word_rid = self.request.GET.get('query_text_rid')
        q_date = self.request.GET.get('query_date')
        if q_word_mid:
            object_list = Customer_Machine_Recipe.objects.select_related('Machine_model','Setting_item').filter(\
                    Q(Machine_model__Customer_machine_id__contains=q_word_mid)|Q(Machine_model__Customer_machine_id__icontains=q_word_mid))
        
                           
        elif q_word_rid:
            object_list = Customer_Machine_Recipe.objects.select_related('Machine_model','Setting_item').filter(\
                    Q(Setting_item__Setting_item_id__contains=q_word_rid)|Q(Setting_item__Setting_item_id__icontains=q_word_rid))
                                
        
        elif q_date:
            object_list = Customer_Machine_Recipe.objects.select_related('Machine_model','Setting_item').filter(\
                Q(Customer_machine_input_date__contains=q_date)|\
                    Q(Customer_machine_input_date__icontains=q_date))
                       
        else:
            object_list = Customer_Machine_Recipe.objects.select_related('Machine_model','Setting_item').order_by('-Customer_machine_input_date')
     
                    
        return object_list
################################################################################
class CustomerMachineRecipeCreateView(CreateView):
    

    template_name = 'user_conf/customer_machine_recipe_create.html'
    model = Customer_Machine_Recipe
    form_class = CustomerMachineRecipeCreateForm
    
    success_url = reverse_lazy("main_app:customer_machine_recipe") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'コース設定'
        ctx['msg'] = '装置運転コースの登録が出来ます。'
        return ctx
    
################################################################################
class CustomerMachineRecipeUpdateView(UpdateView):

    template_name = 'user_conf/customer_machine_recipe_update.html'
    model = Customer_Machine_Recipe
    form_class = CustomerMachineRecipeUpdateForm
    
    success_url = reverse_lazy("main_app:customer_machine_recipe") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = 'コース設定'
        ctx['msg'] = '装置運転コースの変更が出来ます。'
        return ctx

################################################################################
class CustomerMachineRecipeDeleteView(DeleteView):
    

    template_name = 'user_conf/customer_machine_recipe_delete.html'
    model = Customer_Machine_Recipe
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:customer_machine_recipe") 
 
