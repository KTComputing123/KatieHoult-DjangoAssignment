from django.urls import path

from UWEFlix import views


urlpatterns = [
    path("", views.home, name="home"),
    path("user_login/", views.user_login, name="user_login"),
    path("ManageAccountsList/", views.ManageAccountsList, name="ManageAccountsList"),
    path("ManageAccountsCreate/", views.ManageAccountsCreate, name="ManageAccountsCreate"),
    path("ManageAccountsEdit/<str:pk>/", views.ManageAccountsEdit, name="ManageAccountsEdit"),
    path("ManageAccountsDelete/<str:pk>/", views.ManageAccountsDelete, name="ManageAccountsDelete"),
]