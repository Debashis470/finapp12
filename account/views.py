from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Info
from .serializers import InfoSerializer
from django.http import HttpResponse



def home(request):
    return HttpResponse("Account app is working!")
@api_view(['GET'])
def get_info_list(request):
    infos = Info.objects.all()
    serializer = InfoSerializer(infos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_info(request):
    serializer = InfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
