import django_filters
from app_smart.models import Sensor, TemperaturaData, ContadorData, UmidadeData, LuminosidadeData
from rest_framework import permissions
from app_smart.api import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q


class SensorFilter(django_filters.FilterSet):
    responsavel = django_filters.CharFilter(field_name='responsavel', lookup_expr='icontains')
    status_operacional = django_filters.CharFilter(field_name='status_operacional', lookup_expr='iconstains')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='iconstains')
    localizacao = django_filters.CharFilter(field_name='tipo', lookup_expr='iconstains')

    class Meta:
        model = Sensor
        fields = ['status_operacional', 'tipo', 'localizacao', 'responsavel']


class TemperaturaDataFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(field_name = 'timestamp', lookup = 'gte') 
    timestamp_lte = django_filters.DateTimeFilter(field_name = 'timestamp', lookup = 'lte')
    sensor = django_filters.NumberFilter(field_name='sensor')
    valor_gte = django_filters.NumberFilter(field_name = 'valor', lookup='gte')       
    valor_lte = django_filters.NumberFilter(field_name = 'valor', lookup='lte') 

    class Meta:
        model = TemperaturaData 
        fields = ['timestamp_gte', 'timestamp_lte', 'sensor', 'valor_gte', 'valor_lte']     
    

class TemperaturaFilterView(APIView):
    permissions_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)   


        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)        
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)     
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)


        queryset = TemperaturaData.objects.filter(filters) 
        serializer = serializers.TemperaturaDataSerializer(queryset, many=True)
        return Response(serializer.data)       
    
    
class ContadorFilterView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)


        queryset = ContadorData.objects.filter(filters)
        count = queryset.count()
        serializer = serializers.ContadorDataSerializer(queryset, many=True)

        response_data = {
            'count':count, 
            'results': serializer.data
        }    

        return Response(response_data)
    

class UmidadeDataFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(field_name = 'timestamp', lookup = 'gte')
    timestamp_lte = django_filters.DateTimeFilter(field_name = 'timestamp', lookup= 'lte')         
    sensor = django_filters.NumberFilter(field_name = 'sensor')       
    valor_gte = django_filters.NumberFilter(field_name = 'valor', lookup = 'gte') 
    valor_lte = django_filters.NumberFilter(field_name = 'vcalor', lookup = 'lte')

    class Meta:
        model = UmidadeData 
        fields = ['timestamp_gte', 'timestamp_lte', 'sensor', 'valor_gte', 'valor_lte'] 


class UmidadeFilterView(APIView):
    permissions_classes = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        
        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)        
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)     
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)


        queryset = UmidadeData.objects.filter(filters)
        serializer = serializers.UmidadeDataSerializer(queryset, many = True)
        return Response(serializer.data)
    
    



class LuminosidadeDataFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(field_name= 'timestamp', lookup = 'gte')
    timestamp_lte = django_filters.DateTimeFilter(field_name = 'timestamp', lookup= 'lte')         
    sensor = django_filters.NumberFilter(field_name = 'sensor')       
    valor_gte = django_filters.NumberFilter(field_name = 'valor', lookup = 'gte') 
    valor_lte = django_filters.NumberFilter(field_name = 'vcalor', lookup = 'lte')        

    class Meta:
        model = LuminosidadeData
        fields = ['timestamp_gte', 'timestamp_lte', 'sensor', 'valor_gte', 'valor_lte']

class LuminosidadeFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        
        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)        
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)     
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)

        queryset = LuminosidadeData.objects.filter(filters)
        serializer = serializers.LuminosidadeDataSerializer(queryset, many = True)
        return Response(serializer.data) 
