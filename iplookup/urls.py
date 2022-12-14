
from django.contrib import admin
from django.urls import path, include
from .views import IpLookup, HomeView,now
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView, name='home'),
    path('iplookup/',IpLookup , name='iplookup'),
    path('iplookup/<str:pk>',now , name='now'),
    # path('iplookup/<str:pk>',iplookup , name='iplookup1'),
    path('whois/',HomeView, name='whois'),
    path('dns/', HomeView, name='dns'),
    path('proxy/', HomeView, name='proxy'),
    path('tools/', HomeView, name='tools'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
