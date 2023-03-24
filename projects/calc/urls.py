from django.urls import path 
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home,name='home'),
    path('add',views.add,name='add'),
    path('articles/', views.articles,name='articles'),
    # path('register/', views.userreg,name='userreg'),
    path('register/insertuser',views.insertuser,name='insertuser')

]

urlpatterns +=staticfiles_urlpatterns()