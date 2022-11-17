from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path('store', views.store, name="store"),
    path('attendance', views.show, name="attendance"),
    path('token', views.create_token, name="create_token")
]