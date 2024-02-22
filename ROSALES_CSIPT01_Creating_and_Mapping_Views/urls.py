from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vision/', views.vision),
    path('mission/', views.mission),
    path('objectives/', views.objectives),
]
