from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board.models import Board


def writeform(request):
    # POST방식으로 들어올려는 사람 못들어오게
    # 인증 체크(보안처리)
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')


def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    return render(request, 'board/list.html', context)


def view(request):
    id = request.GET.get('id', False) #<primary key>면 get
                                #filter는 <특정조건에 맞는 Row>
    board = Board.objects.get(id=id)
    result = {'board': board}

    return render(request, 'board/view.html', result)


def write(request):
    return render(request, 'board/write.html')


def add(request):
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.user_id = request.POST['user_id']

    board.save()

    return HttpResponseRedirect('/board')

def writeform(request):
    data = request.session['authuser']['id']
    print('data ====== ', data)
    return render(request, 'board/write.html', {'id': data})


def modify(request):
    id = request.GET.get('id', False)
    board = Board.objects.get(id=id)
    result = {'board': board}
    return render(request, 'board/modify.html', result)

def modifyform(request):
    board = request.objects.get(id='id')
    print('board=======================', board)

    board.title = request.GET.get('title')
    board.content = request.GET.get('content')

    board.save()

    return HttpResponseRedirect('/board/modify')










