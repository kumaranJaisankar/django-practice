from django.urls import path 
from . import views 

urlpatterns = [
    
    path('accounts/register',views.registerform,name ='index'),
    path('accounts/login',views.login,name='login'),
    path('',views.indexs,name='index'),
    path('logout/',views.logout,name='logout')
   
    

]