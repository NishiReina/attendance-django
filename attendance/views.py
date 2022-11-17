from django.shortcuts import render, redirect
from attendance.models import Attendance
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import string
import secrets

# Create your views here.

@login_required
def index(request):
    return render(request, 'attendance/index.html')

@csrf_exempt
def store(request):
    jsonData = request.POST['data']
    if jsonData == 'Hello':
        attendance = Attendance.objects.filter(posted_at__date = date.today()).filter(user = request.user)
        if attendance.first() is None:
            Attendance.objects.create(user=request.user)

    return redirect('/attendance')

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


def create_pass(request):
    # パスワードの桁数
    size = 12
    # 英数文字列(大文字含む)、記号から選択
    pool = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([secrets.choice(pool) for _ in range(size)])

    context = {
        'password' : password
    }

    return render(request, 'attendance/token.html', context)
