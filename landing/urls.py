from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.Landing.as_view(), name='index')
]
