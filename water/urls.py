"""
URL configuration for water project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from waterGIS import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from waterGIS.views import *

urlpatterns = [

    # This is where all your app's URLs are included
    path('', views.home, name='home'),


    path("admin/", admin.site.urls),
    path('', include('waterGIS.urls')),
    path('home2/', views.home2_view, name='home2'),







] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
