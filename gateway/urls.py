from django.urls import path

from predictions.views import SolarWindPredictionView

urlpatterns= [
    path("prediction/dwmy/", SolarWindPredictionView.as_view(), name="daily_prediction"),

    
]