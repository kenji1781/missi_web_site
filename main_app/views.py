from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
#from .forms import LoginForm
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'index.html'
index = IndexView.as_view()


class BasicConfView(TemplateView):
    template_name = 'basicconf.html'
conf = BasicConfView.as_view()



"""
def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう１つのページです。',
        'goto':'index',
    }
    return render(request, 'index.html', params)
"""