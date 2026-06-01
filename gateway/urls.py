from django.urls import path

from predictions.views import SolarPredictionView

urlpatterns= [
    path("prediction/daily/", SolarPredictionView.as_view(), name="daily_prediction"),

    
]