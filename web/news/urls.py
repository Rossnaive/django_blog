
from django.conf.urls import url, include
from .import views
app_name = 'news'


urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^cate/(?P<cate>[0-9]+)/$', views.cate, name = 'cate'),
    url(r'^detail/(?P<detail>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^email/$', views.email, name='email'),
#    url(r'^success/$', views.success, name='success')
]
