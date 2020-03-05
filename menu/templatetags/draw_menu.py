from django.db import models
from django import template
from ..models import SubMenu, Menu
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import Http404


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, title_menu, request_item):
	active_item = get_object_or_404(SubMenu, menu=title_menu, parent=None)
	try:
		active_item_menu = SubMenu.objects.get(named_url=request_item, menu = title_menu)
	except ObjectDoesNotExist:
		pass
	else:
		return active_item_menu
	return active_item
	

@register.simple_tag(takes_context=True)
def draw_menu_children(context, children):
	menu_item = get_object_or_404(SubMenu, pk=children)
	return menu_item