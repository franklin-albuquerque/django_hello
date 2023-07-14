from django.urls import path
from app_hello import views

urlpatterns = [
    path('', views.hello, name='hello')
]
