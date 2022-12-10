from rest_framework import serializers

from .models import Container, Report

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'container',
            'red_sensor', 'blue_sensor', 'green_sensor', 
            'proximity_sensor_1', 'proximity_sensor_2', 'proximity_sensor_3', 
            "servomotor_1", 'servomotor_2', 'servomotor_3',
        ]