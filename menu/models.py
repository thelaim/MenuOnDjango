from django.db import models

class Menu(models.Model):
	menu_title = models.CharField(max_length=64, primary_key=True)

	def __str__(self):
		return self.menu_title

class SubMenu(models.Model):
	named_url = models.CharField(max_length=100, blank=True, null=True, unique=True)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
	sub_menu_title = models.CharField(max_length=64)

	def __str__(self):
		return self.sub_menu_title

	def children(self):
		return self.submenu_set.all()

