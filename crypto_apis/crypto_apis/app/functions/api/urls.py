from django.urls import path
from . import views
from . import main
from .apps import BTCRatesAPIConfig as Config

app_name = Config.name

urlpatterns = [
    path(
        "extract",
        views.BTCRatesAPI.as_view(),
        name = "btc-usd-rate-extract",
    ),
    path(        
        "insert-tickers",
        main.insert_to_tickers_table,
        name = "insert-tickers",
    ),
    path(        
        "insert-btc-rates",
        main.insert_to_historical_table,
        name = "insert-btc-rates",
    ),
    path(
        "get-historical-data",
        views.ReturnBTCRatesAPI.as_view(),
        name = "get-historical-data",
    ),
    path(
        "get-historical-data-csv",
        views.ReturnBTCRatesCSVAPI.as_view(),
        name = "get-historical-data-csv",
    )
]
