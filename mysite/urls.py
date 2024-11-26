"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap

# development time imports
import debug_toolbar
from django.urls import path  
from website.views import maintenance 
# ------------------------

from django.conf import settings
from django.urls import re_path
# from django.conf.urls import handler404

handler404 = 'website.views.custom_404'

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap
}


urlpatterns = [
    path('maintenance/', maintenance, name='maintenance'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('website.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt', include('robots.urls')),
    path("__debug__/", include(debug_toolbar.urls)),
    path('summer_note/', include('django_summernote.urls')),
    path(r'captcha/', include('captcha.urls')), 
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
