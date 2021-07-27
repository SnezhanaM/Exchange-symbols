import requests
import json


def unified_name(base, quote):
    return base + '/' + quote


data_dict = {}

r = requests.get('https://aws.okex.com/api/spot/v3/instruments')
for i in json.loads(r.text):
    data_dict[unified_name(i['base_currency'], i['quote_currency'])] = ['', i['instrument_id']]

r = requests.get('https://api.binance.com/api/v3/exchangeInfo')
for i in json.loads(r.text)['symbols']:
    if unified_name(i['baseAsset'], i['quoteAsset']) in data_dict.keys():
        data_dict[unified_name(i['baseAsset'], i['quoteAsset'])][0] = i['symbol']
    else:
        data_dict[unified_name(i['baseAsset'], i['quoteAsset'])] = [i['symbol'], '']

for k in sorted(data_dict.keys()):
    print(k, data_dict[k][0], data_dict[k][1], sep=',')
