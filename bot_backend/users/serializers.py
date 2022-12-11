from rest_framework import serializers

from .models import CustomerProfile, User, Session

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',"first_name", "last_name", 'role']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = CustomerProfile
        fields = ["user", "points", "phone_number", "chat_id"]

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ["date", "id", "points"]