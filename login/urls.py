from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^profile$', views.profile.as_view(), name='profile'),
]
