from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def writeform(request):
    #POST방식으로 들어올려는 사람 못들어오게
    #인증 체크(보안처리)
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')


def modifyform(request):
    return render(request, '/board/modifyform')