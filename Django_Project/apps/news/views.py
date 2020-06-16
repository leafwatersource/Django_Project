import time
from django import http
from django.shortcuts import render

IP_PULL = {}
def func(fun):
    def fff(request):
        now_time = time.time()
        ip = request.META.get('REMOTE_ADDR')
        if ip not in IP_PULL:
            IP_PULL[ip] = [now_time]
        has = IP_PULL.get(ip)
        while has and now_time - has[-1] >1:
            has.pop()
        if (len(has))<3:
            has.insert(0,now_time)
            return fun(request)
        else:
            request.session['ipname'] = ip
            request.session.set_expiry(300)
            return http.HttpResponseForbidden()
    return fff


# Create your views here.
@func
def index(request):
    return render(request,'news/index.html')

def news_detail(request):
    return render(request,'news/news_detail.html')

def search(request):
    return render(request,'news/search.html')