from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Trouble_History,Customer_Machine,Trouble_Contents
from django.contrib import messages
from datetime import datetime,date,time
#from django.utils.timezone import localdate,localtime
from ..plugin_plotly import GraphGenerator
import numpy as np
import pandas as pd
from django_pandas.io import read_frame



class LossTimeGraphView(TemplateView):
    template_name = 'monitoring/losstime_graph.html'

    def get_context_data(self,**kwargs):
        ctx = super().get_context_data(**kwargs)
        
        ctx['title'] = 'ロスタイム集計'
        ctx['msg'] = 'ロスタイム詳細確認が出来ます。'
        

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

        queryset = Trouble_History.objects.filter(Trouble_occurrence_time__year=year)
        queryset = queryset.filter(Trouble_occurrence_time__month=month)
           
        if not queryset:
            return ctx
        
        
        df = read_frame(queryset,fieldnames=['Trouble_occurrence_time','Trouble_loss_time','Machine_model'])
        
        gen = GraphGenerator()

        # pieチャートの素材を作成
        df_pie = pd.pivot_table(df,index='Machine_model',values='Trouble_loss_time',aggfunc=np.sum)
        
        pie_labels = list(df_pie.index.values)
        pie_values = [val[0] for val in df_pie.values]
        plot_pie = gen.month_pie(labels=pie_labels, values=pie_values)
        ctx['plot_pie'] = plot_pie

        # テーブルでのカテゴリと金額の表示用。
        # {カテゴリ:金額,カテゴリ:金額…}の辞書を作る
        ctx['table_set'] = df_pie.to_dict()['Trouble_loss_time']

        # totalの数字を計算して渡す
        ctx['total_payment'] = df['Trouble_loss_time'].sum()

        # 日別の棒グラフの素材を渡す
        df_bar = pd.pivot_table(df, index='Trouble_occurrence_time', values='Trouble_loss_time', aggfunc=np.sum)
        dates = list(df_bar.index.values)
        heights = [val[0] for val in df_bar.values]
        plot_bar = gen.month_daily_bar(x_list=dates, y_list=heights)
        ctx['plot_bar'] = plot_bar
        
        return ctx