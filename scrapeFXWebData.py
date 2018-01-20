# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from datetime import date
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer

# r = requests.get('http://www.xe.com/currencytables/?from=USD&date=2015-12-15')
#
# soup = BeautifulSoup(r.text)
# currencyTable = soup('table')[0]
# curr = []
# for tr in currencyTable('tr'):
#    if tr.find('td') is not None:
#        curr.append([td.text for td in tr('td')])
#
#
# with open('D:\\Users\\Floyd\\Documents\\Projects\\CurrencyExchangeRates\\fx_rates.csv', 'w') as f:
#    writer = csv.writer(f, lineterminator='\n')
#    writer.writerows(curr)


def get_fx_rates_oanda(rate_date):
    """
    Get daily currency exchange rates from oanda.com.

    Given the date, a post request is sent to oanda.com to query their historical
    daily exchange rates. The response is parsed to extract the exchange rates into
    a list.

    Parameters
    ----------
    rate_date : datetime.date
        The date of the currency exchange rate

    Returns
    -------
    rates : list
        A list of lists containing currency code, currency name, rate (USD/1 unit) and
        rate date for 160+ currencies for the given date
    """
    # date string for http post
    datehttppost = '{:%m%%2F%d%%2F%y}'.format(dt)

    # header information for post request
    headers = {
        'Origin':                    'http://www.oanda.com',
        'Accept-Encoding':           'gzip, deflate',
        'Accept-Language':           'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Content-Type':              'application/x-www-form-urlencoded',
        'Accept':                    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control':             'max-age=0',
        'Referer':                   'http://www.oanda.com/currency/table',
        'Connection':                'keep-alive'
    }

    # data for post request. will be used in the query
    data = 'value=1&date=' + datehttppost + '&date_fmt=us&result=1&lang=en&exch=USD&exch2=&Currency=GBP'
    data += '&Currency=JPY&Currency=CHF&Currency=CAD&Currency=AFN&Currency=ALL&Currency=DZD'
    data += '&Currency=ADF&Currency=ADP&Currency=AOA&Currency=AON&Currency=ARS&Currency=AMD'
    data += '&Currency=AWG&Currency=AUD&Currency=ATS&Currency=AZM&Currency=AZN&Currency=BSD'
    data += '&Currency=BHD&Currency=BDT&Currency=BBD&Currency=BYR&Currency=BEF&Currency=BZD'
    data += '&Currency=BMD&Currency=BTN&Currency=BOB&Currency=BAM&Currency=BWP&Currency=BRL'
    data += '&Currency=BND&Currency=BGN&Currency=BIF&Currency=XOF&Currency=XAF&Currency=XPF'
    data += '&Currency=KHR&Currency=CVE&Currency=KYD&Currency=CLP&Currency=CNY&Currency=COP'
    data += '&Currency=KMF&Currency=CDF&Currency=CRC&Currency=HRK&Currency=CUC&Currency=CUP'
    data += '&Currency=CYP&Currency=CZK&Currency=DKK&Currency=DJF&Currency=DOP&Currency=NLG'
    data += '&Currency=XEU&Currency=XCD&Currency=ECS&Currency=EGP&Currency=SVC&Currency=EEK'
    data += '&Currency=ETB&Currency=EUR&Currency=FKP&Currency=FJD&Currency=FIM&Currency=FRF'
    data += '&Currency=GMD&Currency=GEL&Currency=DEM&Currency=GHC&Currency=GHS&Currency=GIP'
    data += '&Currency=XAU&Currency=GRD&Currency=GTQ&Currency=GNF&Currency=GYD&Currency=HTG'
    data += '&Currency=HNL&Currency=HKD&Currency=HUF&Currency=ISK&Currency=INR&Currency=IDR'
    data += '&Currency=IRR&Currency=IQD&Currency=IEP&Currency=ILS&Currency=ITL&Currency=JMD'
    data += '&Currency=JOD&Currency=KZT&Currency=KES&Currency=KWD&Currency=KGS&Currency=LAK'
    data += '&Currency=LVL&Currency=LBP&Currency=LSL&Currency=LRD&Currency=LYD&Currency=LTL'
    data += '&Currency=LUF&Currency=MOP&Currency=MKD&Currency=MGA&Currency=MGF&Currency=MWK'
    data += '&Currency=MYR&Currency=MVR&Currency=MTL&Currency=MRO&Currency=MUR&Currency=MXN'
    data += '&Currency=MDL&Currency=MNT&Currency=MAD&Currency=MZM&Currency=MZN&Currency=MMK'
    data += '&Currency=ANG&Currency=NAD&Currency=NPR&Currency=NZD&Currency=NIO&Currency=NGN'
    data += '&Currency=KPW&Currency=NOK&Currency=OMR&Currency=PKR&Currency=XPD&Currency=PAB'
    data += '&Currency=PGK&Currency=PYG&Currency=PEN&Currency=PHP&Currency=XPT&Currency=PLN'
    data += '&Currency=PTE&Currency=QAR&Currency=ROL&Currency=RON&Currency=RUB&Currency=RWF'
    data += '&Currency=WST&Currency=STD&Currency=SAR&Currency=RSD&Currency=SCR&Currency=SLL'
    data += '&Currency=XAG&Currency=SGD&Currency=SKK&Currency=SIT&Currency=SBD&Currency=SOS'
    data += '&Currency=ZAR&Currency=KRW&Currency=ESP&Currency=LKR&Currency=SHP&Currency=SDD'
    data += '&Currency=SDP&Currency=SDG&Currency=SRD&Currency=SRG&Currency=SZL&Currency=SEK'
    data += '&Currency=SYP&Currency=TWD&Currency=TJS&Currency=TZS&Currency=THB&Currency=TOP'
    data += '&Currency=TTD&Currency=TND&Currency=TRY&Currency=TRL&Currency=TMM&Currency=TMT'
    data += '&Currency=USD&Currency=UGX&Currency=UAH&Currency=UYU&Currency=AED&Currency=UZS'
    data += '&Currency=VUV&Currency=VEB&Currency=VEF&Currency=VND&Currency=YER&Currency=YUN'
    data += '&Currency=ZMW&Currency=ZMK&Currency=ZWD&expr2=&format=CSV&dest=Get+Table'

    # proxy, if needed
    proxies = {
    }

    # submit post to oanda.com
    req = requests.post('http://www.oanda.com/currency/table', headers=headers, data=data,
                        proxies=proxies)

    # from the response, extract only the table containing the exchange rates
    soup = BeautifulSoup(req.text, 'lxml', parse_only=SoupStrainer(id='converter_table'))

    # within the html table, the rate data are contained in the <pre> tag
    ratetable = soup('pre')
    rates = []
    for row in ratetable:
        # keep text only, strip all html/xml tags
        txt = str(row.text)
        # txt variable is one long string of data
        # split the string into lines then split the lines into individual data elements
        # the slice [2:] excludes the header row and blank line after it
        for line in txt.split('\n')[2:]:
            if line != '':
                # the slice excludes the 1 unit/USD conversion
                rates.append(line.split(',')[0:3] + [rate_date])

    return rates

if __name__ == '__main__':
    dt = date(2015, 12, 31)
    new_rates = get_fx_rates_oanda(dt)
    with open('fx_rates.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(new_rates)
