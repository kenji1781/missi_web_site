from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう１つのページです。',
        'goto':'index',
    }
    return render(request, 'index.html', params)