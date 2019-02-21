from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('newPerson/', views.newPerson, name="index"),
    path('all/', views.all, name="index"),
    path('moreThan21/', views.moreThan21, name="index"),
    path('update/', views.update, name="index"),
]