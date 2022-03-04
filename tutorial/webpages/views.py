from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def response_test(request):
    return HttpResponse('helloo world')

forloop_exmp = [1,2,3,4,5]
if_exmp = True
def template_test_1(request):
    return render(request,'index.html',{ 'name': 'hello world1', "forloop_exmp": forloop_exmp, "if_exmp": if_exmp})

def template_test_2(request):
    return render(request, 'secondary.html', { 'name': 'hello world1', "forloop_exmp": forloop_exmp, "if_exmp": if_exmp})