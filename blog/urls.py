from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/$', views.PostView.as_view(), name='post'),
    url(r'^post/(?P<pk>[0-9]+)$', views.ShowPost.as_view(), name='certain_post')
]