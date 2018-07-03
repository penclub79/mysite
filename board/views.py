from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board


def writeform(request):
    #POST방식으로 들어올려는 사람 못들어오게
    #인증 체크(보안처리)
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')


def modifyform(request):
    return render(request, '/board/modifyform')

def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    return render(request, 'board/list.html', context)

def view(request):
    return render(request, 'board/view.html')

def viewform(request):
    pass
    # boardmodify = Board()
    # return HttpResponseRedirect(request, '/board')

def write(request):
    return render(request, 'board/write.html')

def writeform(request):
    board = Board()
    board.title = request.POST['title']
    board.name = request.POST['name']
    board.hit = request.POST['hit']
    board.regdate = request.POST['regdate']
    board.user = request.POST['user']

    board.save()

    return HttpResponseRedirect('/board')


def modify(request):
    return render(request, 'board/modify.html')



