from django.views.decorators.http import require_POST 
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, Http404
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.exceptions import ValidationError

from .serializers import ContainerSerializer, ReportSerializer
from .models import Container

from users.models import CustomerProfile, Session, User
from users.serializers import SessionSerializer


class ContainerList(ListAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


class UpdateContainer(UpdateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


@require_POST
def report_post(request):
    data = JSONParser().parse(request)
    is_active = True
    for value in data.values()[1:]:
        if value == False:
            is_active = False
            break
    container = Container.objects.filter(pk=data['container']).update(is_active=is_active)
    serializer = ReportSerializer(data=data).save()
    return JsonResponse(serializer.data)
    
    


@require_POST
@csrf_exempt
def session_post(request):
    data = JSONParser().parse(request)
    user = get_object_or_404(User, rfid=data['rfid'])
    if user in User.objects.fiter(role="Customer"):
        return 
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
    
