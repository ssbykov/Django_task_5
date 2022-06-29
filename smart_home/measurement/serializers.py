from rest_framework import serializers

from measurement.models import Sensor, Measurement


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):

   class Meta:
       model = Measurement
       fields = ['temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

