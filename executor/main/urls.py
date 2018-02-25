from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/dashboard', views.usrDashboard, name='usrDashboard'),
    path('protector/dashboard', views.ptrDashboard, name='ptrDashboard'),
    path('court/dashboard', views.crtDashboard, name='crtDashboard'),
    path('contract/jorda', views.contractDetail, name='contractDetail'),
]

