from django.urls import path

from . import views

app_name='Account'
urlpatterns = [
    path('login/',views.userLoginView.as_view(),name='user_login'),
    path('register/',views.userRegisterView.as_view(),name='user_register'),
    path('logout/',views.userLogoutView.as_view(),name='user_logout'),
]
