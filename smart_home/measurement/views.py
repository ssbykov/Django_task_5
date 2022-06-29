# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorsSerializer


class SensorApi(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        name = request.GET.get('name')
        description = request.GET.get('description')
        if name:
            Sensor(name=name, description=description).save()
            return Response({'status': f'датчик {name} добавлен.'})
        else:
            return Response({'status': 'параметр name отсутствует'})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        name = request.GET.get('name')
        try:
            sensor = Sensor.objects.get(id=int(pk))
            if name:
                sensor.name = name
            sensor.description = request.GET.get('description')
            sensor.save()
            return Response({'status': f'датчик с id={id} изменен.'})
        except:
            return Response({'status': f'датчик с id={id} отсутствует.'})


@api_view(['POST'])
def measurement(request):
    sensor_id = request.GET.get('sensor_id')
    temperature = request.GET.get('temperature')
    try:
        Measurement(sensor_id=sensor_id, temperature=temperature).save()
        return Response({'status': 'измерение добавлено.'})
    except:
        return Response({'status': f'не задан один из параметров, либо датчик с id={sensor_id} отсутствует'})
