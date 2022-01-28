from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Equipment_Category
from ..forms import EquipmentCategoryCreateForm,EquipmentCategoryUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class EquipmentCategoryView(LoginRequiredMixin,ListView):
    
    template_name = 'manufacturer_setting/equipment_category.html'
    model = Equipment_Category
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '装置カテゴリー'
        ctx['msg'] = '装置カテゴリーの確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Equipment_Category.objects.filter(Q(Equipment_category__contains=q_word)|Q(Equipment_category__icontains=q_word))
        elif q_date:
            object_list = Equipment_Category.objects.filter(Equipment_category_input_date=q_date)
        else:
            object_list = Equipment_Category.objects.order_by('-Equipment_category_input_date')


        return object_list
################################################################################
class EquipmentCategoryCreateView(CreateView):
    

    template_name = 'manufacturer_setting/equipment_category_create.html'
    model = Equipment_Category
    form_class = EquipmentCategoryCreateForm
    
    success_url = reverse_lazy("main_app:equipment_category") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '装置カテゴリー'
        ctx['msg'] = '装置カテゴリーの登録が出来ます。'
        return ctx
    
################################################################################
class EquipmentCategoryUpdateView(UpdateView):

    template_name = 'manufacturer_setting/equipment_category_update.html'
    model = Equipment_Category
    form_class = EquipmentCategoryUpdateForm
    
    success_url = reverse_lazy("main_app:equipment_category") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '装置カテゴリー'
        ctx['msg'] = '装置カテゴリーの変更が出来ます。'
        return ctx

################################################################################
class EquipmentCategoryDeleteView(DeleteView):
    

    template_name = 'manufacturer_setting/equipment_category_delete.html'
    model = Equipment_Category
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:equipment_category") 
 
