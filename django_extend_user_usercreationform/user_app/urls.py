from django.urls import path
from user_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('show/', views.show, name='show'),
]
