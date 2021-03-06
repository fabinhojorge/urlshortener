"""urlshortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from core.views import index, url_redirect, url_statistics

urlpatterns = [
    path('', index, name='index'),
    re_path('(?P<link_short>[\w]{10})\+/', url_statistics, name='short_url_detail'),
    re_path('(?P<link_short>[\w]{10})/', url_redirect, name='short_url_redirect'),
]
