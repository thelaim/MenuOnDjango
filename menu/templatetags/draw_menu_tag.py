from django.db import models
from django import template
from ..models import SubMenu, Menu

register = template.Library()

@register.inclusion_tag('templates/draw_menu.html')
def draw_menu(title_menu):
	#menu = Menu.objects.filter(menu_title=title_menu)
	context = SubMenu.objects.select_related().filter(menu=title_menu)
	return context
