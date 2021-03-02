from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PlandataForm,Todo_addForm,CompletionForm
from .models import Plandata,Completion
from django.core.paginator import Paginator
import datetime

# Create your views here.
#予定の一覧表示(ホーム画面)
def index(request, num=1):
    td = datetime.date.today()
    td_week = td + datetime.timedelta(days=7)
    data = Plandata.objects.all().order_by('toki')
    page = Paginator(data,10)
    params = {
            'title':'ようこそ',
            'message':'今後の予定一覧', 
            'td_week':td_week,
            'td':td,
            'data':page.get_page(num),
    }
    return render(request, 'todo/home.html',params)

#予定の追加
def add(request):
    errormessage = ''
    if(request.method == 'POST'):
        tmp = Plandata()
        plandata = PlandataForm(request.POST, instance=tmp)
        if plandata.is_valid():
            plandata.save()
            return redirect(to='/home')
        else:
            errormessage = '正しく入力がされていません'
    params = {
            'title':'予定の追加',
            'message':'予定を追加します',
            'errormessage':errormessage,
            'form': Todo_addForm() 
    }
    return render(request, 'todo/todo_add.html',params)

#予定情報の更新
def updata(request, num):
    errormessage = ''
    target_data = Plandata.objects.all().get(id=num)
    if(request.method == 'POST'):
        plandata = PlandataForm(request.POST, instance=target_data)
        if plandata.is_valid():
            plandata.save()
            return redirect(to='/home')
        else:
            errormessage = '正しく入力がされていません'
    item = {
        'toki':target_data.toki,
        'basho':target_data.basho,
        'naiyo':target_data.naiyo,
    }
    params = {
        'title':'予定の更新',
        'message':'予定を更新します',
        'errormessage':errormessage,
        'id': num,
        'form': Todo_addForm(initial=item),
    }
    return render(request, 'todo/todo_updata.html',params)

#予定の完了
def complete(request, num):
    kanryo_day = datetime.date.today()
    complete_data = Plandata.objects.all().get(id=num)
    if(request.method == 'POST'):
        tmp = Completion()
        item = {
            'toki':complete_data.toki,
            'kanryo_day':kanryo_day,
            'basho':complete_data.basho,
            'naiyo':complete_data.naiyo,
        }
        completion = CompletionForm(item,instance=tmp)
        completion.save()
        complete_data.delete()
        return redirect(to='/home')
    params = {
        'title':'予定の完了',
        'message':'予定を完了します',
        'id': num,
        'kanryo_day': kanryo_day,
        'data':complete_data,
    }
    return render(request, 'todo/todo_complete.html',params)


#予定の削除
def delete(request, num):
    delete_data = Plandata.objects.all().get(id=num)
    if(request.method == 'POST'):
        delete_data.delete()
        return redirect(to='/home')
    params = {
        'title': '予定の削除',
        'message':'予定を削除します',
        'id':num,
        'data':delete_data
    }
    return render(request, 'todo/todo_delete.html',params)

#予定一覧の並び替え
def sort(request, num):
    td = datetime.date.today()
    tomorrow = td + datetime.timedelta(days=1)
    td_week = td + datetime.timedelta(days=7)
    if(num == 1):
        data = Plandata.objects.all().order_by('toki')
    elif(num == 2):
        data = Plandata.objects.filter(toki=td)
    elif(num == 3):
        data = Plandata.objects.filter(toki__gte=tomorrow,toki__lte=td_week).order_by('toki')
    elif(num == 4):
        data = Plandata.objects.filter(toki__gte=td_week).order_by('toki')
    else:
        data = Plandata.objects.all().order_by('id')
    page = Paginator(data,10)
    params = {
            'title':'ようこそ',
            'message':'今後の予定一覧', 
            'td_week':td_week,
            'tomorrow':tomorrow,
            'td':td,
            'data':page.get_page(1),
    }
    return render(request, 'todo/home.html',params)

def completion_home(request, num=1):
    data = Completion.objects.all().order_by('kanryo_day')
    page = Paginator(data,10)
    params = {
            'title':'完了タスク一覧',
            'message':'完了タスク一覧', 
            'data':page.get_page(num),
    }
    return render(request, 'todo/completion_home.html',params)
