from django.shortcuts import render, redirect
from attendance.models import Attendance
from datetime import date
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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
