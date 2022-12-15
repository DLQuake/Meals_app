from django.shortcuts import render
import requests
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.
def get_meals(request):
    all_meals = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://www.themealdb.com/api/json/v1/1/search.php? s=%s' % name
        response = requests.get(url)
        data = response.json()
        meals = data['meals']

        for i in meals:
            meal_data = Project(
                name = i['strMeal'],
                category = i['strCategory'],
                instructions = i['strInstructions'],
                region = i['strArea'],
                slug = i['idMeal'],
                image_url = i['strMealThumb']
            )
            meal_data.save()
            all_meals = Project.objects.all().order_by('-id')

    return render (request, 'meals/meal.html', { "all_meals": all_meals} )


def meal_detail(request, id):
    meal = Project.objects.get(id = id)
    return render ( request, 'meals/meal_detail.html', {'meal': meal} )


@api_view(['GET'])
def meal_list(request):
    if request.method == 'GET':
        meal = Project.objects.all()
        serializer = ProjectSerializer(meal, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_meal(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def meal_list_detail(request, pk):
    try:
        meal = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        meal = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(meal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(meal, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
