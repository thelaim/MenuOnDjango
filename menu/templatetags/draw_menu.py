from django.db import models
from django import template
from ..models import SubMenu, Menu

register = template.Library()

@register.simple_tag#inclusion_tag('templates/draw_menu.html')
def draw_menu(title_menu):
	menu_title = Menu.objects.get(menu_title=title_menu)
	context = SubMenu.objects.select_related().filter(menu = menu_title)
	return context
