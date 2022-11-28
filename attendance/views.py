from django.shortcuts import render, redirect
from attendance.models import Attendance
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import string
import secrets
from .models import Passcode
from rest_framework import viewsets
from .serializer import PasscodeInfoSerializer

import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@login_required
def index(request):
    return render(request, 'attendance/index.html')

@login_required
@csrf_exempt
def store(request):
    jsonData = request.POST['data']
    passcode = Passcode.objects.filter(created_at__date = date.today()).last()
    if jsonData == passcode.passcode:
        attendance = Attendance.objects.filter(posted_at__date = date.today()).filter(user = request.user)
        if attendance.count() == 0:
            Attendance.objects.create(user=request.user)

    # return redirect('/attendance')
    return render(request, 'attendance/done.html')

@login_required
def show(request):
    if request.method== 'POST':
        attendances = Attendance.objects.filter(posted_at__date = request.POST['date'])
        day = request.POST['date']
    else:
        attendances = Attendance.objects.filter(posted_at__date = date.today())
        day = date.today()

    context = {
        'attendances' : attendances,
        'day' : day
    }
    return render(request, 'attendance/attendance.html', context)


@login_required
@ensure_csrf_cookie
def create_pass(request):
    # パスワードの桁数
    size = 12
    # 英数文字列(大文字含む)、記号から選択
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([secrets.choice(pool) for _ in range(size)])

    passcode = Passcode.objects.filter(created_at__date = date.today())
    if passcode.count() == 0:
        Passcode.objects.create(passcode = password)

    passcode = Passcode.objects.filter(created_at__date = date.today()).first()

    # passcode = Passcode.objects.all()

    # return passcode
    context = {
        'passcode' : passcode
    }

    return render(request, 'attendance/token.html', context)    

    # context = {
    #     'password' : password
    # }

    # json_str = json.dumps(context, ensure_ascii=False, indent=2)

    # # return render(request, 'attendance/token.html', context)
    # response = HttpResponse(json_str,content_type='application/json; charset=UTF-8', status=status)
    # return response

class PasscodeInfoViewSet(viewsets.ModelViewSet):

    # パスワードの桁数
    size = 5
    # 英数文字列(大文字含む)、記号から選択
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(size)])
    
    passcode = Passcode.objects.filter(created_at__date = date.today())
    if passcode.count() == 0:
        Passcode.objects.create(passcode = password)

    # モデルのオブジェクトを取得
    data = Passcode.objects.filter(created_at__date = date.today()).last()
    id = data.id
    queryset = Passcode.objects.filter(id=id)
    # シリアライザーを取得
    serializer_class = PasscodeInfoSerializer