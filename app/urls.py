from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_successful, name='login-view')
]