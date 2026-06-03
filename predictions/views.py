from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from services.weather_service import fetch_weather_data
from ml.model import SolarWindModel


class SolarWindPredictionView(APIView):

    def get(self, request):
        
        temperature = float(request.GET.get("temperature", 25))
        cloud_cover = float(request.GET.get("cloud_cover", 20))
        radiation = float(request.GET.get("radiation", 800))
        humidity = float(request.GET.get("humidity", 50))
        wind_speed = float(request.GET.get("wind_speed", 10))
        panel_capacity = float(request.GET.get("panel_capacity", 20))

        panels = int(request.GET.get("panels", 10))
        panels_capacity = int(request.GET.get("panels_capacity", 300))

        sun_hours = float(request.GET.get("sun_hours", 6))

        rotor_area = int(request.GET.get("rotor_area", 10))
        hub_height = int(request.GET.get("hub_height", 50))
        


        model = SolarWindModel()

        results = [[
             temperature,
             cloud_cover,
             radiation,
             panels,
             panel_capacity,
             sun_hours,
             humidity,
             wind_speed,
             rotor_area,
             hub_height,

        ]]

        daily_energy, daily_power = model.predict(results)
        weekly_energy = daily_energy * 7
        monthly_energy = daily_energy * 30
        yearly_energy = daily_energy * 365


             
        

        
     

               
        return Response({
            
            "temperature": temperature,
            "cloud_cover": cloud_cover,
            "radiation": radiation,
            "panels":panels,
            "panel_capacity": panel_capacity,
            "sun_hours": sun_hours,
            "daily_solar_predicted_energy_in_kWh": daily_energy,
            "weekly_solar_predicted_energy_in_kWh": weekly_energy,
            "monthly_solar_predicted_energy_in_kWh": monthly_energy,
            "yearly_solar_predicted_energy_in_kWh": yearly_energy,


            "humidity": humidity,
            "wind_speed": wind_speed,
            "rotor_area": rotor_area,
            "hub_height": hub_height,
            "daily_wind_predicted_power_in_kWh": daily_power,
            "weekly_wind_predicted_power_in_kWh": daily_power * 7,
            "monthly_wind_predicted_power_in_kWh": daily_power * 30,
            "yearly_wind_predicted_power_in_kWh": daily_power * 365,


        
        })
    

        
        
        

        

