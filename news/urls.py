from django.contrib import admin
from django.urls import path,include
from subscribe import urls as subscribe_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(subscribe_urls))
]
