from django.db import models
from rest_framework import serializers
from .models import Tickers, Historical

class TickersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tickers
        fields = '__all__'

class HistoricalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Historical
        fields = '__all__'