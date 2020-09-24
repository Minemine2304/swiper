from django.http import JsonResponse


# Create your views here.
from UserApp.logics import send_vcode


def ferch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code':0,'data':None})
    else:
        return JsonResponse({'code': 1000, 'data': None})

def sumbit_vcode(request):
    '''提交验证码，执行登陆注册'''
    return JsonResponse()

def show_profile(request):
    '''查看个人资料'''
    return JsonResponse()

def update_profile(request):
    '''更新个人资料'''
    return JsonResponse()

def qn_token(request):
    '''获取七牛云 Token'''
    return JsonResponse()

def qn_callback(request):
    '''七牛云回调接口'''
    return JsonResponse()
