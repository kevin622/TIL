from django.urls import path
from . import views

# practice0309/...
urlpatterns = [
    path('var_route/<int:value>/', views.var_route),
    path('lotto/<value>', views.lotto),
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),
]
