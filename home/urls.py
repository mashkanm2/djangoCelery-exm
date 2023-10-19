from django.urls import path,include
from .views import postBlogView,homeView

app_name='home'

urlpatterns = [
    path('',homeView.as_view(),name='home'),
    path('company/<slug:company_slug>/',homeView.as_view(), name='company_filter'),
    path('<slug:slug>/',postBlogView.as_view(),name='post_detail')
]
