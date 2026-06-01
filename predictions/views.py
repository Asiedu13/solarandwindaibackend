from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from services.weather_service import fetch_weather_data
from ml.model import SolarModel


class SolarPredictionView(APIView):

    def get(self, request):
        
        temperature = float(request.GET.get("temperature", 25))
        cloud_cover = float(request.GET.get("cloud_cover", 20))
        radiation = float(request.GET.get("radiation", 800))
        panel_capacity = float(request.GET.get("panel_capacity", 20))

        panels_min = int(request.GET.get("panels_min", 10))
        panels_max = int(request.GET.get("panels_max", 12))

        sun_min = float(request.GET.get("sun_min", 4))
        sun_max = float(request.GET.get("sun_max", 6))
        sun_step = float(request.GET.get("sun_step", 0.5))
    


        model = SolarModel()

        results = []

        panels = panels_min

        while panels <= panels_max:

            sun_hours = sun_min

            while sun_hours <= sun_max:

                X = [[temperature, cloud_cover, radiation, panels, panel_capacity, sun_hours]]

                energy = model.predict(X)[0]

                results.append({
                    "panels": panels,
                    "sun_hours": sun_hours,
                    "predicted_energy_kwh": energy
                })

                sun_hours += sun_step

            panels += 1
        return Response(results)

        

