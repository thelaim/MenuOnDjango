from django.shortcuts import render
from .models import SubMenu
from django.db.models.aggregates import Count
from django import template # нужен для регистрации шаблонного тега
from django.core.context_processors import csrf

register = template.Library()
@register.inclusion_tag('templates/draw_menu.html') # регистрация шаблона для подключения 

def get_menu(request):
    context = {}
    context['categorys'] = SubMenu.objects.select_related().all()
    return context
