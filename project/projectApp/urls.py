from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/',views.meal_detail, name = "meal_detail"),
    path('listmeals/', views.meal_list),
    path('listmeals/add', views.add_meal),
    path('listmeals/<int:pk>/', views.meal_list_detail),
]