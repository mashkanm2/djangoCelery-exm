from django.urls import path

from . import views

appname='Account'
urlpatterns = [
    path('login/',views.userLoginView.as_view(),name='login'),
    path('register/',views.userRegisterView.as_view(),name='register'),
    path('logout/',views.userLogoutView.as_view(),'logout'),
]
