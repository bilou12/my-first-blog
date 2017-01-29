from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^inscription/', views.inscription, name='inscription'),
    url(r'^$', views.home, name='home'),
]