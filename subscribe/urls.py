from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe', views.SubscriptionView, name='subscribe'),
    path('verify/<str:token>', views.verify),
]
