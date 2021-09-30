from django.urls import path
from .views import index, main, req, oxford, scrap

urlpatterns = [
    path('index', index, name='index'),
    path('main/page', main, name='main'),
    path('request/page', req, name='request'),
    path('oxford/page', oxford, name='ox'),
    path('scrap/page', scrap, name='scrap'),
]
