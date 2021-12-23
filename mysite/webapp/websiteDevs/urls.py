from django.urls import path, include
from .. import views

urlpatterns = [
    path('', views.info),
    path('members/', views.members),
    path('devs/', views.developers),
]