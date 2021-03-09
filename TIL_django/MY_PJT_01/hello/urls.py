from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.hi, name='hi'),
    path('me_too/', views.me_too, name='me_too')
]
