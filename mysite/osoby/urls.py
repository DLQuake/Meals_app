from django.urls import path
from osoby import views

urlpatterns = [
    path("", views.home, name="home"),
]