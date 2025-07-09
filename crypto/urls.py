from django.urls import path
from . import views


urlpatterns =[
    path('register/', views.register, name = "register"),
    path('login/', views.login, name = "login"),
    path('dashboard/', views.dashboard, name = "dashboard" ),
    path('share/', views.share, name = "share" ),
    path('home/',views.home, name = "home"),

]