from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from ..models import Unit_Price_Electric,Unit_Price_Electric
from ..forms import ElectricPriceCreateForm,ElectricPriceUpdateForm
from django.db .models import Q



class IndexView(TemplateView):
    template_name = 'index.html'



