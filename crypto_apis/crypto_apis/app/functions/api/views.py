import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Tickers
from .serializers import TickersSerializer
from app.functions.extract.main import Extract

class BTCRatesAPI(APIView):

        def get(self, request):
            try:    
                if request.method == 'GET' and 'product_id' in request.GET:
                    product_id = request.GET.get('product_id')
                    extract = Extract(product_id)
                    response = extract.main()

                    return Response(response, status = status.HTTP_200_OK)

                return Response("Bad Request: Missing Product ID", status = status.HTTP_400_BAD_REQUEST)

            except Exception as error:
                error_message = f"Error: {error}!"
                return Response(error_message, status = status.HTTP_503_SERVICE_UNAVAILABLE)

class ReturnBTCRatesAPI(APIView):

        def get(self, request):
            try:    
                if request.method == 'GET' and 'product_id' in request.GET:
                    product_id = request.GET.get('product_id')
                    start_date = int(request.GET.get('start_timestamp'))
                    end_date = int(request.GET.get('end_timestamp'))

                    extract = Extract(product_id, start_date, end_date)
                    response = extract.get_historical_data()

                    return Response(response, status = status.HTTP_200_OK)

                return Response("Bad Request: Missing Product ID", status = status.HTTP_400_BAD_REQUEST)

            except Exception as error:
                error_message = f"Error: {error}!"
                return Response(error_message, status = status.HTTP_503_SERVICE_UNAVAILABLE)


class ReturnBTCRatesCSVAPI(APIView):

    def get(self, request, format=None):
        try:
            if request.method == 'GET' and 'product_id' in request.GET:
                product_id = request.GET.get('product_id')
                start_date = int(request.GET.get('start_timestamp'))
                end_date = int(request.GET.get('end_timestamp'))
                extract = Extract(product_id, start_date, end_date)
                response_json = extract.get_historical_data()
                response = HttpResponse(
                        content_type='text/csv',
                        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
                    )
                writer = csv.DictWriter(response, fieldnames=['date', 'low', 'high', 'open', 'close', 'ticker_id', 'percentage_change'])
                for data in response_json:
                    writer.writerow(data)
                return response
            return Response("Bad Request: Missing Product ID", status = status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            error_message = f"Error: {error}!"
            return Response(error_message, status = status.HTTP_503_SERVICE_UNAVAILABLE)
