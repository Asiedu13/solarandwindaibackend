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

        panels = int(request.GET.get("panels", 10))
        panels_capacity = int(request.GET.get("panels_capacity", 300))

        sun_hours = float(request.GET.get("sun_hours", 6))
        


        model = SolarModel()

        results = [[
             temperature,
             cloud_cover,
             radiation,
             panels,
             panel_capacity,
             sun_hours
        ]]

        energy = model.predict(results)[0]


             
        

        
     

               
        return Response({
            "temperature": temperature,
            "cloud_cover": cloud_cover,
            "radiation": radiation,
            "panels":panels,
            "panel_capacity": panel_capacity,
            "sun_hours": sun_hours,
            "predicted_energy_in_kWh": energy
        })

        

