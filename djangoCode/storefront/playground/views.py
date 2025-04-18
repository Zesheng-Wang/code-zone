from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 1
    y = 2
    return x + y


# Create your views here.
def say_hello(request):
    # 可以从数据库中提取数据
    # 可以转换数据
    # 发送邮件等等
    # return HttpResponse("Hello World!")
    x = calculate()
    y = 2
    context = {"name": "Zesheng"}
    return render(request, "hello.html", context=context)
