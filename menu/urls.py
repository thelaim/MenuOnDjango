from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.menu, name='menu'),
]