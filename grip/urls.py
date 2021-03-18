
from django.urls import path , include
from . import views
from django.urls import path, include
from . import models 

urlpatterns = [
    path('',views.home,name="home"),
    path("showcustomer",views.showcustomer,name="showcustomer"),
    path("profile",views.profile,name="profile"),
    path("transfermoney",views.transfermoney,name='transfermoney'),
    path("transferhistory",views.transferhistory,name='transferhistory'),

]
