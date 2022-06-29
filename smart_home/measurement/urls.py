from django.urls import path

from measurement.views import SensorApi, measurement, SensorView

urlpatterns = [
    path('sensors/', SensorApi.as_view()),
    path('sensors/<id>/', SensorApi.as_view()),
    path('measurement/', measurement),
    path('sensor/<pk>/', SensorView.as_view()),

]
