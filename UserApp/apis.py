

from django.http import JsonResponse
from django.core.cache import cache

# Create your views here.
from UserApp.logics import send_vcode
from UserApp.models import User, Profile


def ferch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code':0,'data':None})
    else:
        return JsonResponse({'code': 1000, 'data': '验证码发送失败'})

def sumbit_vcode(request):
    '''提交验证码，执行登陆注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    key = 'Vcode-%s' % phonenum
    cached_vcode = cache.get(key)

    if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum) #从数据库获取用户
        except User.DoesNotExist:
    #         如果用户不存在，则执行注册流程注册
            user = User.objects.create(phonenum=phonenum,nickname=phonenum)

    #     在session中记录用户登陆的状态
        request.session['uid'] = user.id

        return JsonResponse({'code': 0,'data': user.to_dict()})
    else:
        return JsonResponse({'code':1001,'data':'验证码错误'})

def show_profile(request):
    '''查看个人资料'''
    uid = request.session['uid']
    profile, _ = Profile.objects.get_or_create(id=uid)
    return JsonResponse({'code':0,'data': profile.to_dict()})

def update_profile(request):
    '''更新个人资料'''
    return JsonResponse()

def qn_token(request):
    '''获取七牛云 Token'''
    return JsonResponse()

def qn_callback(request):
    '''七牛云回调接口'''
    return JsonResponse()
