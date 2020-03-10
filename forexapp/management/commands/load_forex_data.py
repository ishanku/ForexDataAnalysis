from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from forexapp.models import ForexCurrent,ForexHistoric
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'


ALREADY_LOADED_ERROR_MESSAGE = """
data already loaded"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from csv into our model"

    def handle(self, *args, **options):
        if ForexCurrent.objects.exists() and ForexHistoric.objects.exists():
            print('ForexCurrent data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading Forex Current Data")
        for fl in DictReader(open('./Resources/2020_forex.csv')):
            forex=ForexCurrent()
            forex.Date=fl['Date']
            forex.AUD=fl['AUD']
            forex.EUR=fl['EUR']
            forex.NZD=fl['NZD']
            forex.GBP=fl['GBP']
            forex.BRL=fl['BRL']
            forex.CAD=fl['CAD']
            forex.CNY=fl['CNY']
            forex.HKD=fl['HKD']
            forex.INR=fl['INR']
            forex.KRW=fl['KRW']
            forex.MXN=fl['MXN']
            forex.ZAR=fl['ZAR']
            forex.SGD=fl['SGD']
            forex.DKK=fl['DKK']
            forex.JPY=fl['JPY']
            forex.MYR=fl['MYR']
            forex.NOK=fl['NOK']
            forex.SEK=fl['SEK']
            forex.LKR=fl['LKR']
            forex.CHF=fl['CHF']
            forex.TWD=fl['TWD']
            forex.THB=fl['THB']
            forex.save()
        print("Loading ForexHistorical Data")
        for fl in DictReader(open('./Resources/forexhistorical.csv')):
            forex=ForexHistoric()
            forex.Date=fl['Date']
            forex.AUD=fl['AUD']
            forex.EUR=fl['EUR']
            forex.NZD=fl['NZD']
            forex.GBP=fl['GBP']
            forex.BRL=fl['BRL']
            forex.CAD=fl['CAD']
            forex.CNY=fl['CNY']
            forex.HKD=fl['HKD']
            forex.INR=fl['INR']
            forex.KRW=fl['KRW']
            forex.MXN=fl['MXN']
            forex.ZAR=fl['ZAR']
            forex.SGD=fl['SGD']
            forex.DKK=fl['DKK']
            forex.JPY=fl['JPY']
            forex.MYR=fl['MYR']
            forex.NOK=fl['NOK']
            forex.SEK=fl['SEK']
            forex.LKR=fl['LKR']
            forex.CHF=fl['CHF']
            forex.TWD=fl['TWD']
            forex.THB=fl['THB']
            forex.save()
