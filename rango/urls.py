from django.urls import path
from django.conf.urls import url
from rango import views

<<<<<<< HEAD

=======
>>>>>>> dd0868081831c03af2305318197fe6aaa6af62a7
app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    ]
