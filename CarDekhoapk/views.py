from django.shortcuts import render
from .models import CarList
from CarDekhoapk.api_file.serilizer import CarListSerializer
from rest_framework .response import Response
from rest_framework import status
from rest_framework.decorators import api_view,action
from rest_framework import viewsets

# from django.http import JsonResponse
# # can we show date using httpresonce? --> Yes
# from django.http import HttpResponse
# import json
# # Create your views here.
# # before restframe work do this type of things
# def carlist(request):
#     cars= CarList.objects.all()
#     data={
#         'cars':list(cars.values()),
#     }
#     data_json =json.dumps(data)
#     return HttpResponse(data_json, content_type='application/json')# this is method to achive json response
#     #return JsonResponse(data)

# def cardetails(request,pk):
#     car= CarList.objects.get(pk=pk)
#     data={
#         'car_name':car.car_name,
#         'car_description':car.car_description,
#         'car_price':car.car_price,
#     }
#     return JsonResponse(data)



@api_view(['GET', 'POST'])
def carlist(request):
    if request.method == 'GET':
        try:
            cars = CarList.objects.all()
            serializer = CarListSerializer(cars, many=True)
            
        except CarList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = CarListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cardetails(request, pk):
    if request.method == 'GET':
        try:
            car = CarList.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serilizer = CarListSerializer(car)
        return Response(serilizer.data)
    if request.method == 'PUT':
        car = CarList.objects.get(pk=pk)
        serializer = CarListSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    if request.method == 'DELETE':
        car = CarList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    
            

        



