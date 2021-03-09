from django.urls import path, include
from . import views
urlpatterns = [
    path('lotto/', views.lotto)
]
