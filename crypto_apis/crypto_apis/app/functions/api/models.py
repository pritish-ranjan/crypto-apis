from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField


class Tickers(models.Model):
    
    name = models.TextField()

    def __str__(self):
        return self.name

class Historical(models.Model):
    date = models.DateTimeField()
    low = models.DecimalField(max_digits = 10,
                         decimal_places = 5)
    high = models.DecimalField(max_digits = 10,
                         decimal_places = 5)
    open = models.DecimalField(max_digits = 10,
                         decimal_places = 5)
    close = models.DecimalField(max_digits = 10,
                         decimal_places = 5)
    ticker_id = models.IntegerField()

    def __str__(self):
        return str(self.ticker_id)
