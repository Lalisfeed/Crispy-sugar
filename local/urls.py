from django.urls import path
from . import views

app_name = "local"
urlpatterns = [
    path('', views.auth, name="auth"), # authentication page for all users
    path('menu/', views.orders, name="orders"), # make orders looking at the menu
    path('settings/', views.settings, name="settings"), # add or remove items in menu
    path('orders/', views.history, name="history"), # list past orders

    path('offline/', views.offline, name="offline"), # page to load when offline
    path('<str:error>', views.error, name="error"), # incorrect path
    path('<str:error>/', views.error, name="error"), # incorrect path
]

