from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Machine_Drive_History
from django.contrib import messages
from datetime import datetime,date,time
#from django.utils.timezone import localdate,localtime
from ..plugin_plotly import GraphGenerator
import numpy as np
import pandas as pd
from django_pandas.io import read_frame
from ..machine_drive_history_model_comp import ModelComplement
from django.contrib.auth.mixins import LoginRequiredMixin


class WorkHistoryGraphView(LoginRequiredMixin,TemplateView):
    template_name = 'monitoring/work_history_graph.html'

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        
        ctx['title'] = '稼働詳細'
        ctx['msg'] = '稼働詳細確認が出来ます。'
        

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

        queryset = Machine_Drive_History.objects.filter(Data_datetime__year=year)
        queryset = queryset.filter(Data_datetime__month=month)
           
        if not queryset:
            return ctx
        
        #稼働履歴モデルの補完を行う##########################
        modelcomp = ModelComplement()
        #datetimeをdateとtimeに分割
        modelcomp.datetime_complement(queryset)
        #idから機種を書込み
        modelcomp.machine_model_complement(queryset)
        #各最新単価を書込み
        modelcomp.unit_cost_complement(queryset)
        #################################################
        df = read_frame(queryset,fieldnames=['Data_date','Customer_recipe_no','Machine_model'])
        
        gen = GraphGenerator()

        # pieチャートの素材を作成
                
        #円グラフ
        pie_labels = df['Customer_recipe_no']#トラブル名を渡す
        pie_values = df['Customer_recipe_no'].value_counts()#件数を渡す
        plot_pie = gen.month_pie(labels=pie_labels, values=pie_values)
        ctx['plot_pie'] = plot_pie



        
        # テーブルでのカテゴリと金額の表示用。
        # {カテゴリ:金額,カテゴリ:金額…}の辞書を作る
        ctx['table_set'] = pie_values

        # totalの数字を計算して渡す
        ctx['total_payment'] = pie_values.sum()

        df['count'] = len(df)
        # 日別の棒グラフの素材を渡す
        df_bar = pd.pivot_table(df, index='Data_date', values='count')
        dates = list(df_bar.index.values)
        heights = [val[0] for val in df_bar.values]
        
          
        ctx['transition_plot'] = gen.transition_plot(x_list_payment=dates,
                                                   y_list_payment=heights)
        
        return ctx


        