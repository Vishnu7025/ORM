from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>home page </h1>")

def page2(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled')
    request.session.delete_test_cookie()
    return HttpResponse("<b> page2 </b>")

def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])
    count= 1
    response = render(request,'count.html',{'count':count})
    response.set_cookie('count',count)