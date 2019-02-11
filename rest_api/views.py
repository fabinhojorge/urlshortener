from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_api.serializers import UrlSerializer
from rest_api.models import Url


@api_view(['GET'])
def urlList(request):
    list_url = Url.objects.all()
    serializer = UrlSerializer(list_url, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def createUrl(request):

    data = JSONParser().parse(request)

    if Url.objects.filter(link=data['link']).exists():
        serializer = UrlSerializer(Url.objects.get(link=data['link']), data=data)
    else:
        serializer = UrlSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
