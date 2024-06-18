from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import Sensor, TemperaturaData, ContadorData, UmidadeData, LuminosidadeData

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_password):
        validated_password['password'] = make_password(validated_password['password'])
        return super().create(validated_password)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class TemperaturaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaData
        fields = '__all__'        


class ContadorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContadorData 
        fields = '__all__'


class UmidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmidadeData 
        fields = '__all__'        

class LuminosidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuminosidadeData 
        fields = '__all__'