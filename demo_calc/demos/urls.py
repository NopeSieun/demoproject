from django.urls import path
from . import views

app_name = 'demos'

urlpatterns = [
    path('', views.calculator, name='calculator'),
]