
from django.contrib import admin
from django.urls import path
from triplet import views


urlpatterns = [
    path('', views.home, name='home'),  # Serves your HTML page
    path('api/', views.index, name='api_index'),  # Your API view
]