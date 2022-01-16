from datetime import datetime
from .models import Tickers, Historical
from .serializers import TickersSerializer, HistoricalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# add exception handling

@api_view(['POST'])
def insert_to_tickers_table(request):
    if request.method=="POST":
        insert_tickers_serializer = TickersSerializer(data=request.data)
        if insert_tickers_serializer.is_valid():
            insert_tickers_serializer.save()
            return Response(insert_tickers_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def insert_to_historical_table(request):
    if request.method=="POST":
        request.data["date"] = datetime.fromtimestamp(request.data["date"])
        insert_historical_serializer = HistoricalSerializer(data=request.data)
        if insert_historical_serializer.is_valid():
            insert_historical_serializer.save()
            return Response(insert_historical_serializer.data, status=status.HTTP_201_CREATED)

def internal_insert_to_historical_table(request):
    request["date"] = datetime.fromtimestamp(request["date"])
    insert_historical_serializer = HistoricalSerializer(data=request)
    if insert_historical_serializer.is_valid():
        insert_historical_serializer.save()
        return ("Record created in the database Historical table!")