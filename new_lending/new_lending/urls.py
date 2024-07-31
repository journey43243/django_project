"""
URL configuration for new_lending project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.defaults import page_not_found

from new_lending import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('',include('lending.urls', namespace='lending')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('authentication/',include('authentication.urls',namespace= 'authentication')),
    path('',include('cart.urls', namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler_404 = page_not_found
admin.site.site_header = "Administration panel"
admin.site.index_title = "Data"