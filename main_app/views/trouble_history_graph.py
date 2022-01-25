from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Trouble_History,Customer_Machine,Trouble_Contents
from ..forms import TroubleHistoryCreateForm,TroubleHistoryUpdateForm
from django.db .models import Q
from django.contrib import messages
from datetime import datetime,date,time
from ..plugin_plotly import GraphGenerator
import numpy as np
import pandas as pd
from django_pandas.io import read_frame



################################################################################
class TroubleHistoryView(ListView):
    
    template_name = 'monitoring/trouble_history.html'
    model = Trouble_History
    paginate_by = 10

    
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)

        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の確認／変更が出来ます。'

        object_list = []

        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))

        ctx['year_month'] = f'{year}年{month}月'

        #前月と次月をコンテキストに入れて渡す。
        if month == 1:
            prev_year = year - 1
            prev_month = 12
        else:
            prev_year = year
            prev_month = month - 1

        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1

        ctx['prev_year'] = prev_year
        ctx['prev_month'] = prev_month
        ctx['next_year'] = next_year
        ctx['next_month'] = next_month
        

        #グラフ処理
        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Trouble_History.objects.filter(\
                    Q(Customer_machine_id__contains=q_word)|Q(Customer_machine_id__icontains=q_word))
                        
        else:
            object_list = Trouble_History.objects.filter(Trouble_occurrence_time__year=year)
            object_list = object_list.filter(Trouble_occurrence_time__month=month).order_by('-Trouble_occurrence_time')
            

        if not object_list:
            return ctx
        
        
        
        df = read_frame(object_list,fieldnames=['Trouble_contents','Trouble_occurrence_time'])
        
        gen = GraphGenerator()

        #円グラフ
        pie_labels = df['Trouble_contents']#トラブル名を渡す
        pie_values = df['Trouble_contents'].value_counts()#件数を渡す
        plot_pie = gen.month_pie(labels=pie_labels, values=pie_values)
        ctx['plot_pie'] = plot_pie
        
        #棒グラフ
        # 日別の棒グラフの素材を渡す
        dates = df['Trouble_occurrence_time']
        heights = df['Trouble_contents'].value_counts()#件数を渡す
        plot_bar = gen.month_daily_bar(x_list=dates, y_list=heights)
        ctx['plot_bar'] = plot_bar
        
        return ctx
        

    def get_queryset(self):

        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))

        q_word = self.request.GET.get('query_text')
        q_date = self.request.GET.get('query_date')
        if q_word:
            object_list = Trouble_History.objects.filter(\
                    Q(Customer_machine_id__contains=q_word)|Q(Customer_machine_id__icontains=q_word))
                        
        else:
            object_list = Trouble_History.objects.filter(Trouble_occurrence_time__year=year)
            object_list = object_list.filter(Trouble_occurrence_time__month=month).order_by('-Trouble_occurrence_time')

            for history in object_list:
                if (history.Trouble_occurrence_time != None)and(history.Trouble_recovery_time != None):
                    date1 = history.Trouble_recovery_time    
                    date2 = history.Trouble_occurrence_time
                    loss_time = date1-date2
                    history.time_calc = loss_time.total_seconds()
                    history.Trouble_loss_time = str(loss_time)
                    history.save()

                if (history.Customer_machine_id != None)and(history.Machine_model == None):
                    for c_machine in Customer_Machine.objects.select_related('Machine_model').all():
                        #for t_contents in Trouble_Contents.objects.select_related('Machine_model').all():
                        if history.Customer_machine_id == history.Customer_machine_id:
                                history.Machine_model = str(c_machine.Machine_model)+ ': #' +str(c_machine.Customer_machine_unit_no)                   
                                history.save()
                
                if (history.Trouble_no != None)and(history.Trouble_contents == None):
                    for t_contents in Trouble_Contents.objects.select_related('Machine_model').all():
                         if history.Trouble_no == t_contents.Trouble_no:
                                history.Trouble_contents = t_contents.Trouble_contents                   
                                history.save()        
                

        return object_list
################################################################################
class TroubleHistoryCreateView(CreateView):
    

    template_name = 'monitoring/trouble_history_create.html'
    model = Trouble_History
    form_class = TroubleHistoryCreateForm
    
    success_url = reverse_lazy("main_app:trouble_history") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の登録が出来ます。'
        return ctx
    
################################################################################
class TroubleHistoryUpdateView(UpdateView):

    template_name = 'monitoring/trouble_history_update.html'
    model = Trouble_History
    form_class = TroubleHistoryUpdateForm
    
    success_url = reverse_lazy("main_app:trouble_history") 

#unique=True時**kwargs記述のこと
    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        # page_title を追加する
        ctx['title'] = '異常履歴'
        ctx['msg'] = '異常履歴の変更が出来ます。'
        return ctx

################################################################################
class TroubleHistoryDeleteView(DeleteView):
    

    template_name = 'monitoring/trouble_history_delete.html'
    model = Trouble_History
    #form_class = ElectricPriceCreateForm
    
    success_url = reverse_lazy("main_app:trouble_history") 
 
