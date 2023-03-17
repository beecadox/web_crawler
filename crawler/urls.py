"""crawler URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crawler/', include('backend.urls')),
    path('', include('frontend.urls'))
]
