from django.urls import  path
from Newapp import views

app_name = 'Newapp'

urlpatterns =[
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path("user_logout",views.user_logout,name="user_logout"),
    path("image",views.image,name="image"),
    path("members",views.members,name='members')
]