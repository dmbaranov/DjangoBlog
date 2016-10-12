from django.conf.urls import url
from . import views

app_name = 'authorization'
urlpatterns = [
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^result/$', views.AuthResultView.as_view(), name='result'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^user/(?P<pk>[0-9]+)$', views.ShowUser.as_view(), name='user')
]