from django.contrib import admin
from django.urls import path
from authontication.views import*


urlpatterns = [
    path('', home,name='home'),
    path('login/',user_login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',user_logout, name='logout'),

]


