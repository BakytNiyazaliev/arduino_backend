# from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from .models import CustomerProfile, Session, User
from .serializers import CustomerSerializer, SessionSerializer, UserSerializer

class CustomersList(ListAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerSerializer


def get_customer(request, phone_number):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        object = get_object_or_404(CustomerProfile, phone_number=phone_number)
        serializer = CustomerSerializer(data=data)
        serializer.update
    return JsonResponse(serializer.data)


def get_customer_by_chat_id(request, chat_id):
    object = get_object_or_404(CustomerProfile, chat_id=chat_id)
    serializer = CustomerSerializer(object)
    return JsonResponse(serializer.data)


@require_GET
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

def get_history(request, phone_number):
    customer = get_object_or_404(CustomerProfile, phone_number=phone_number)
    queryset = Session.objects.filter(customer=customer).order_by('-id')[:10]
    serializer = SessionSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

