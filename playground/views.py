from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, World!")

def say_hello_html(request):
    # 데이터 전달 : context, 딕셔너리 형태
    return render(request, 'playground/hello.html', {'name':'미림'})


def say_bye(request):
    return render(request, 'playground/bye.html')