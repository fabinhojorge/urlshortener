from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_api.serializers import UrlSerializer
from rest_api.models import Url


@csrf_exempt
@api_view(['POST'])
def create_url(request):

    data = JSONParser().parse(request)

    if Url.objects.filter(link=data['link']).exists():
        serializer = UrlSerializer(Url.objects.get(link=data['link']), data=data)
    else:
        serializer = UrlSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
