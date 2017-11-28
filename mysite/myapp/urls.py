
#dairylogin/urls.py

import sys
from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.core.management import execute_from_command_line

urlpatterns = [
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
	url(r'^helloworld/$', views.TestView.as_view()),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
