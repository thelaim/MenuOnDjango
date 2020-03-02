from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu, name='get_menu'),
]