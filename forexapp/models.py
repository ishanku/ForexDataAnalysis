from django.db import models

# Create your models here.
class ForexCurrent(models.Model):
    Date=models.DateField(auto_now=False, auto_now_add=False)
    AUD=models.DecimalField(max_digits=23, decimal_places=2)
    EUR=models.DecimalField(max_digits=23, decimal_places=2)
    NZD=models.DecimalField(max_digits=23, decimal_places=2)
    GBP=models.DecimalField(max_digits=23, decimal_places=2)
    BRL=models.DecimalField(max_digits=23, decimal_places=2)
    CAD=models.DecimalField(max_digits=23, decimal_places=2)
    CNY=models.DecimalField(max_digits=23, decimal_places=2)
    HKD=models.DecimalField(max_digits=23, decimal_places=2)
    INR=models.DecimalField(max_digits=23, decimal_places=2)
    KRW=models.DecimalField(max_digits=23, decimal_places=2)
    MXN=models.DecimalField(max_digits=23, decimal_places=2)
    ZAR=models.DecimalField(max_digits=23, decimal_places=2)
    SGD=models.DecimalField(max_digits=23, decimal_places=2)
    DKK=models.DecimalField(max_digits=23, decimal_places=2)
    JPY=models.DecimalField(max_digits=23, decimal_places=2)
    MYR=models.DecimalField(max_digits=23, decimal_places=2)
    NOK=models.DecimalField(max_digits=23, decimal_places=2)
    SEK=models.DecimalField(max_digits=23, decimal_places=2)
    LKR=models.DecimalField(max_digits=23, decimal_places=2)
    CHF=models.DecimalField(max_digits=23, decimal_places=2)
    TWD=models.DecimalField(max_digits=23, decimal_places=2)
    THB=models.DecimalField(max_digits=23, decimal_places=2)
    
    def __str__(self):
        return self.Date
    class Meta:
        verbose_name_plural = "ForexCurrentRates"
        managed=False
        app_label='forexapp'
        db_table='ForexCurrent'
