"""
URL configuration for healthcare_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Healthcare Backend API",
        default_version='v1',
        description="API for healthcare management system",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
def home(request):
    return JsonResponse({
        "message": "Healthcare Backend Running 🚀",
        "swagger": "/api-docs/swagger/"
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    
    # API Endpoints
    path("api/auth/", include('accounts.urls')),
    path("api/patients/", include('patients.urls')),
    path("api/doctors/", include('doctors.urls')),
    path("api/mappings/", include('mappings.urls')),
    
    # API Documentation
    # path('api-docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('api-docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api-docs/schema.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('api-docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
