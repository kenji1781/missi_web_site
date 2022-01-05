from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Customer_Machine_Recipe,Customer_Machine,Trouble_Contents
from ..forms import CustomerMachineRecipeCreateForm,CustomerMachineRecipeUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class CustomerMachineRecipeView(ListView):
    
    template_name = 'user_conf/customer_machine_recipe.html'
    model = Customer_Machine_Recipe
    paginate_by = 10

    #for recipe_i in Customer_Machine_Recipe.objects.all():
    #    for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
    #        if (recipe_i.Signal_plc_to_sys == True)or\
    #                ((recipe_i.Machine_model==None) and (recipe_i.Customer_machine_id != None))or\
    #                    ((recipe_i.Customer_machine_id == c_machine.Customer_machine_id)and(recipe_i.Machine_model != c_machine.Machine_model)):
    #            for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
    #                if recipe_i.Customer_machine_id == c_machine.Customer_machine_id:
    #                    recipe_i.Machine_model = str(c_machine.Machine_model)+ ': #' +str(c_machine.Customer_machine_unit_no)                   
                                               
                                        
    #        recipe_i.Signal_plc_to_sys = False
    #        recipe_i.save()





    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = 'レシピ'
        ctx['msg'] = 'レシピの確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Customer_Machine_Recipe.objects.filter(\
                    Q(Customer_machine_id__contains=q_word)|Q(Customer_machine_id__icontains=q_word)|\
                        Q(Machine_model__contains=q_word)|Q(Machine_model__icontains=q_word)|\
                            Q(Recipe_id__contains=q_word)|Q(Recipe_id__icontains=q_word)|\
                                Q(Recipe_name__contains=q_word)|Q(Recipe_name__icontains=q_word)|\
                                    Q(Customer_recipe_no__contains=q_word)|Q(Customer_recipe_no__icontains=q_word))        
       
        elif q_date:
            object_list = Customer_Machine_Recipe.objects.filter(\
                Q(Customer_machine_input_date__contains=q_date)|\
                    Q(Customer_machine_input_date__icontains=q_date))
                       
        else:
            object_list = Customer_Machine_Recipe.objects.order_by('-Customer_machine_input_date')
     
    #    for recipe_i in object_list:
    #            if (recipe_i.Signal_plc_to_sys == True)or((recipe_i.Machine_model==None) and (recipe_i.Customer_machine_id != None)):
                    
                    
    #                for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
    #                    if recipe_i.Customer_machine_id == c_machine.Customer_machine_id:
    #                        recipe_i.Machine_model = str(c_machine.Machine_model)+ ': #' +str(c_machine.Customer_machine_unit_no)                   
                                               
                                        
    #                recipe_i.Signal_plc_to_sys = False
    #                recipe_i.save()


        
        
        
        
        
        
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
        ctx['title'] = 'レシピ'
        ctx['msg'] = 'レシピの登録が出来ます。'
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
        ctx['title'] = 'レシピ'
        ctx['msg'] = 'レシピの変更が出来ます。'
        return ctx

################################################################################
class CustomerMachineRecipeDeleteView(DeleteView):
    

    template_name = 'user_conf/customer_machine_recipe_delete.html'
    model = Customer_Machine_Recipe
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:customer_machine_recipe") 
 
