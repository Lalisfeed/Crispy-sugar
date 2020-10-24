from django.urls import path
from . import views

app_name = "local"
urlpatterns = [
    path('', views.auth, name="auth"), # authentication page for all users
    path('menu/', views.menu, name="menu"),  # make orders looking at the menu
    path('orders/', views.orders, name="orders"),  # list past orders
    path('settings/', views.settings, name="settings"), # add or remove items in menu
    path('profile/', views.profile, name="profile"),  # list past orders

    path('offline/', views.offline, name="offline"), # page to load when offline
    path('<str:error>', views.error, name="error"), # incorrect path
    path('<str:error>/', views.error, name="error"), # incorrect path
]
