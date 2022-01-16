#!/usr/bin/env python
import sys
import requests
from app.functions.api import main
from app.functions.api.models import Tickers, Historical
from datetime import datetime

class Extract:
    try:
        def __init__(self, product_id, start_date=None, end_date=None):
            self.product_id = product_id
            self.start_date = start_date
            self.end_date = end_date
            self.url = f"https://api.exchange.coinbase.com/products/{product_id}/candles"
            self.headers = {"Accept": "application/json"}
            self.rates_keys = ['date', 'low', 'high', 'open', 'close', 'ticker_id']
            return

        def get_ticker_id(self):
            try:            
                ticker_id = Tickers.objects.get(name=self.product_id)
                return ticker_id.id

            except Exception as exc:
                raise ValueError('Ticker not found in database!')
    
        def get_historical_data(self):
            try:
                start_date = datetime.fromtimestamp(self.start_date)
                end_date = datetime.fromtimestamp(self.end_date)

                historical_data = list(Historical.objects.filter(date__range=[start_date, end_date]).order_by('date'))
                
                self.rates_keys.append('percentage_change')
                count = 0
                close_rates = []
                output_rates = []
                for data in historical_data:
                    close_rates.append(data.close)
                    if count == 0:
                        percentage_change = 0
                    else: 
                        percentage_change = ((close_rates[count] - close_rates[count-1])/close_rates[count-1]) * 100
                    result_rates = zip(self.rates_keys, [data.date, data.low, data.high, data.open, data.close, data.ticker_id, percentage_change])
                    output_rates.append(dict(result_rates))
                    count +=1
                return output_rates

            except Exception as exc:
                raise ValueError(f"Error details: {exc}")
            
        def main(self):
            ticker_id = self.get_ticker_id()
            response = requests.request("GET", self.url, headers=self.headers)
            rates = response.json()
    
            for rate in rates:
                del rate[5]
                rate.append(ticker_id)
                rates_request = zip(self.rates_keys, rate)
                rates_request = dict(rates_request)
                response_db = main.internal_insert_to_historical_table(rates_request)

            return response_db

    except Exception as error:
        raise Exception("Error occured!", error)

