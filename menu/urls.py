from django.urls import path
from django.conf.urls import url
from . import views
from menu.views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(.*)/$', IndexView.as_view(), name='index'),
]