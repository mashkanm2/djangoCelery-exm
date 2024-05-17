
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.routers import DefaultRouter
from .views import preprocessIndata,dataReciverAsyncApi,dataReciverSyncApi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="CeleryExample",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls',namespace='home')),
    path('account/',include('Account.urls',namespace='account')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('preprocessdata', preprocessIndata.as_view(), name='preprocessdata'),
    path('postproasync', dataReciverAsyncApi.as_view(), name='async_postprocess'),
    path('postprosync', dataReciverSyncApi.as_view(), name='sync_postprocess'),
]
