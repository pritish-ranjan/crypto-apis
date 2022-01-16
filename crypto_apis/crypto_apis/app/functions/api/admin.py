from django.contrib import admin
from .models import Tickers, Historical

admin.site.register(Tickers)
admin.site.register(Historical)
