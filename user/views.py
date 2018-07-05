from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')

def join(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.gender = request.POST['gender']

    user.save() #DB에 저장
    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')


def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    result = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])
    # result는 리스트로 담긴다.

    # 로그인 실패했을 경우
    if len(result) == 0:
    # 다시 로그인 하라고 돌려보내야한다.
        return HttpResponseRedirect('/user/loginform?result=false')

    # login 처리 (인증처리)
    authuser =result[0]
    # <팁> 세션에 저장한다.
    request.session['authuser'] = model_to_dict(authuser)  #저장할때는 딕셔너리 타입으로 바꾸자

    # return HttpResponse(authuser) 성공햇을시 확인하고 싶으면이거 쓰삼
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')

