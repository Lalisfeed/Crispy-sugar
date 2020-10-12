from django.urls import path
from . import views

app_name = "local"
urlpatterns = [
    path('', views.auth, name="auth"),
    path('settings/', views.settings, name="settings"),
    path('order/', views.orders, name="orders"),
]
