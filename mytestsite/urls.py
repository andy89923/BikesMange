"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from bikes.views import hello_view
from bikes.views import list_all

handler404 = "mytestsite.views.error_views.view_404"
handler500 = "mytestsite.views.error_views.view_500"

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^hello/', hello_view),
	url(r'listall/', list_all),
	url(r'', list_all),
]


