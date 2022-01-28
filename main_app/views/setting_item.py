from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Setting_Item
from ..forms import SettingItemCreateForm,SettingItemUpdateForm
from django.db .models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



################################################################################
class SettingItemView(LoginRequiredMixin,ListView):
    
    template_name = 'user_conf/setting_item.html'
    model = Setting_Item
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '品種名'
        ctx['msg'] = '品種名登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Setting_Item.objects.filter(\
                    Q(Setting_item_id__contains=q_word)|Q(Setting_item_id__icontains=q_word)|\
                        Q(Setting_item_name__contains=q_word)|Q(Setting_item_name__icontains=q_word)|\
                            Q(Setting_item_memo__contains=q_word)|Q(Setting_item_memo__icontains=q_word))
        elif q_date:
            object_list = Setting_Item.objects.filter(Q(Setting_item_input_date__contains=q_date)|\
                Q(Setting_item_input_date__icontains=q_date))
        else:
            object_list = Setting_Item.objects.order_by('-Setting_item_input_date')


        return object_list
################################################################################
class SettingItemCreateView(CreateView):
    

    template_name = 'user_conf/setting_item_create.html'
    model = Setting_Item
    form_class = SettingItemCreateForm
    
    success_url = reverse_lazy("main_app:setting_item") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '品種名'
        ctx['msg'] = '品種名の登録が出来ます。'
        return ctx
    
################################################################################
class SettingItemUpdateView(UpdateView):

    template_name = 'user_conf/setting_item_update.html'
    model = Setting_Item
    form_class = SettingItemUpdateForm
    
    success_url = reverse_lazy("main_app:setting_item") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '品種名'
        ctx['msg'] = '品種名登録の変更が出来ます。'
        return ctx

################################################################################
class SettingItemDeleteView(DeleteView):
    

    template_name = 'user_conf/setting_item_delete.html'
    model = Setting_Item
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:setting_item") 
 
