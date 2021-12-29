from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Trouble_Contents
from ..forms import TroubleContentsCreateForm,TroubleContentsUpdateForm
from django.db .models import Q
from django.contrib import messages



################################################################################
class TroubleContentsView(ListView):
    
    template_name = 'manufacturer_setting/trouble_contents.html'
    model = Trouble_Contents
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '異常内容'
        ctx['msg'] = '異常内容登録の確認／変更が出来ます。'
        return ctx

    def get_queryset(self):
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Trouble_Contents.objects.select_related('Machine_model').filter(\
                    Q(Trouble_no__contains=q_word)|Q(Trouble_no__icontains=q_word)|\
                        Q(Trouble_contents__contains=q_word)|Q(Trouble_contents__icontains=q_word)|\
                            Q(Trouble_memo__contains=q_word)|Q(Trouble_memo__icontains=q_word)|\
                                Q(Machine_model__Machine_model__contains=q_word)|Q(Machine_model__Machine_model__icontains=q_word))
        elif q_date:
            object_list = Customer_Machine.objects.select_related('Machine_model').filter(Q(Customer_machine_inst_date__icontains=q_date)|\
                Q(Trouble_input_date__icontains=q_date))
        else:
            object_list = Customer_Machine.objects.select_related('Machine_model').order_by('-Customer_machine_input_date')


        return object_list
################################################################################
class TroubleContentsCreateView(CreateView):
    

    template_name = 'manufacturer_setting/trouble_contents_create.html'
    model = Trouble_Contents
    form_class = TroubleContentsCreateForm
    
    success_url = reverse_lazy("main_app:trouble_contents") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '異常内容'
        ctx['msg'] = '異常内容の登録が出来ます。'
        return ctx
    
################################################################################
class TroubleContentsUpdateView(UpdateView):

    template_name = 'manufacturer_setting/trouble_contents_update.html'
    model = Trouble_Contents
    form_class = TroubleContentsUpdateForm
    
    success_url = reverse_lazy("main_app:trouble_contents") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '異常内容'
        ctx['msg'] = '異常内容登録の変更が出来ます。'
        return ctx

################################################################################
class TroubleContentsDeleteView(DeleteView):
    

    template_name = 'manufacturer_setting/trouble_contents_delete.html'
    model = Trouble_Contents
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:trouble_contents") 
 
