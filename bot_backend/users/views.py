# from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ValidationError

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404


from .models import CustomerProfile, Session, User
from .serializers import CustomerSerializer, SessionSerializer, UserSerializer


class CustomersList(ListAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer

@csrf_exempt
def get_customer(request, phone_number):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        customer = CustomerProfile.objects.filter(phone_number=phone_number).update(chat_id=data['chat_id'])
        customer = get_object_or_404(CustomerProfile, phone_number=phone_number)
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)
    raise HttpResponseBadRequest


@require_POST
@csrf_exempt
def session_post(request, chat_id):
    data = JSONParser().parse(request)
    data['customer'] = get_object_or_404(CustomerProfile, chat_id=chat_id)
    object = Session(customer=data['customer'], points=data['points'])
    serializer = SessionSerializer(data=data)
    if serializer.is_valid():
        object.save()
        return JsonResponse(serializer.data)
    raise ValidationError

@require_GET
@csrf_exempt
def get_customer_by_chat_id(request, chat_id):
    object = get_object_or_404(CustomerProfile, chat_id=chat_id)
    serializer = CustomerSerializer(object)
    return JsonResponse(serializer.data)


@require_GET
@csrf_exempt
def get_user(request, rfid):
    object = get_object_or_404(User, rfid=rfid)
    serializer = UserSerializer(object)
    return JsonResponse(serializer.data)



@require_POST
@csrf_exempt
def login(request):
    data = JSONParser().parse(request)
    user = get_object_or_404(User, username=data['username'], password=data['password'])
    return JsonResponse(UserSerializer(user).data)

@require_GET
@csrf_exempt
def get_history(request, chat_id):
    customer = get_object_or_404(CustomerProfile, chat_id=chat_id)
    queryset = Session.objects.filter(customer=customer).order_by('-id')[:10]
    serializer = SessionSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

