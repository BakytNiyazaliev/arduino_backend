from django.views.decorators.http import require_POST 
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from .serializers import ContainerSerializer
from .models import Container

from users.models import CustomerProfile, Session, User
from users.serializers import SessionSerializer


class ContainerList(ListAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


class UpdateContainer(UpdateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


@csrf_exempt
def session_post(request):
    data = JSONParser().parse(request)
    user = get_object_or_404(User, username=data['customer'])
    data['customer'] = CustomerProfile.objects.get(user=user)
    object = Session(customer=data['customer'], points=data['points'])
    serializer = SessionSerializer(data=data)
    if serializer.is_valid():
        object.save()
        return JsonResponse(serializer.data)
    raise ValidationError

# @require_POST
# def session_post(request):
#     data = JSONParser().parse(request)
#     data['customer'] = CustomerProfile.objects.get(rfid=data['customer'])
#     session = Session(customer=data['customer'], points=data['points'])
#     serializer = SessionSerializer(session)
#     if serializer.is_valid():
#         serializer.save()
#     else:
#         raise ValidationError


#     return JsonResponse(serializer.data)

# @require_POST
# def session_post(request):
#     data = JSONParser().parse(request)
    
