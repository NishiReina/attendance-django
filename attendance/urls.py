from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name="index"),
    path('store', views.store, name="store"),
    path('attendance', views.show, name="attendance"),
    path('pass', views.create_pass, name="pass")
]