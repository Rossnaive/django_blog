from django.conf.urls import url

from .import views

urlpatterns =[
    url(r'^email/$', views.email, name='email'),
    url(r'^Success/$',views.Success, name = 'success'),


]
