from django.conf.urls import url

from . import views

app_name = 'Recipe'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<quote_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.newquote, name='newquote"),
]
