from django.http import HttpResponse
from django.shortcuts import render

from message.models import UserMessage


def get_form(request):
    """

    :param request:
    :return:
    """
    if request.method == 'GET':
        message = UserMessage.objects.filter(pk=1)[0]
        context = {
            "message": message
        }
        return render(request, 'form.html', context)

    return render(request, 'form.html')


def save(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        # 实例化对象
        user_message = UserMessage()

        # 将html的值传入我们实例化的对象.
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        # 调用save方法进行保存
        user_message.save()


def get_info():
    """
    获取数据库中的信息
    :return:
    """
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message)


def save_info():
    """
    步骤：
    实例化对象
    调用save 方法保存
    :return:
    """
    user_messsage = UserMessage()
    user_messsage.name = 'wang'
    user_messsage.email = 'aa@qq.com'
    user_messsage.address = 'beijing'
    user_messsage.message = '你好'

    user_messsage.save()
