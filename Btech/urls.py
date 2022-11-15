"""Btech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from Btech19 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/category_products', views.categorys_view),
    path('api/v1/podcategories', views.podcategories_view),
    path('api/v1/podcategories/Xiaomi', views.xiaomi_view),
    path('api/v1/podcategories/Samsung', views.samsung_view),
    path('api/v1/podcategories/Apple', views.apple_view),
    path('api/v1/podcategories/Huawei', views.huawei_view),
    path('api/v1/podcategories/Honor', views.honor_view),
    path('api/v1/podcategories/HomePhone', views.homephone_view),
    path('api/v1/podcategories/Phone', views.phone_view),
    path('api/v1/podcategories/Naushnicki', views.Naushnicki_view),
    path('api/v1/podcategories/PortativnoeAudio', views.PortativnoeAudio_view),
    path('api/v1/podcategories/VneshnieAkkumulyatori', views.VneshnieAkkumulyatori_view),
    path('api/v1/podcategories/Zaryadnyi_ustr', views.Zaryadnyi_ustr_view),
    path('api/v1/podcategories/Kabeli', views.Kabeli_view),
    path('api/v1/podcategories/Chehly', views.Chehly_view),
    path('api/v1/podcategories/SteklaAndPlenki', views.SteklaAndPlenki_view),
    path('api/v1/podcategories/SD_karta', views.SD_view),
    path('api/v1/podcategories/VseBrendy', views.VseBrendy_view),
    path('api/v1/podcategories/Samsung_Galaxy_Tab', views.Samsung_Galaxy_Tab_view),
    path('api/v1/podcategories/Apple_Ipad', views.Apple_Ipad_view),
    path('api/v1/podcategories/HuweiMatepad', views.HuweiMatepad_view),
    path('api/v1/podcategories/Xiaomi_Tab', views.Xiaomi_Tab_view),
    path('api/v1/podcategories/Tablet_accessories', views.Tablet_accessories_view),
    path('api/v1/podcategories/E-books', views.E_books_view),
    path('api/v1/podcategories/Smart_clock', views.Smartclock_view),
    path('api/v1/podcategories/Fitnes_clock', views.Fitnesclock_view),
    path('api/v1/podcategories/sportclock', views.Sportclock_view),
    path('api/v1/podcategories/Kids_clock', views.Kidsclock_view),
    path('api/v1/podcategories/UmnyeKolonki', views.UmnyeKolonki_view),
    path('api/v1/podcategories/Smart_home', views.Smarthome_view),


]
