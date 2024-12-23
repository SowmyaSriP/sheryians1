from django.urls import path
from .views import *
app_name='app1'
urlpatterns=[
    path('',demo,name='demo'),
    path('code/',code,name='code'),
    path('home/',home,name='home'),
    path('course/',course,name='course'),
    path('boot/',boot,name='boot'),
    path('call/',call,name='call'),
    path('sign/',sign,name='sign'),
    path('impact/',impact,name='impact'),
    path('email/',email,name='email'),
]