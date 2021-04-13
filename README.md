# python-exchangeratesapi
This is an unofficial wrapper for the awesome, partly free [ExchangeRatesAPI](https://exchangeratesapi.io/), which provides exchange rate lookups courtesy of the European Central Bank.

# Installation
Either clone this repository into your project, or install with `pip`:
```
pip install python-exchangeratesapi
```

# Usage
First, you need to register at [ExchangeRatesAPI](https://exchangeratesapi.io/pricing/) for `ACCESS_KEY`.
```py
from exchangeratesapi import Api

api = Api(ACCESS_KEY)

# Get the latest foreign exchange rates:
api.get_rates()

# Get historical rates for any day since 1999:
print(api.get_rates(start_date="2018-03-26"))
{'rates': {'CAD': 1.5997, 'HKD': 9.7384, 'ISK': 121.9, 'PHP': 64.82, 'DKK': 7.4482,
'HUF': 312.73, 'CZK': 25.446, 'AUD': 1.6048, 'RON': 4.6593, 'SEK': 10.1868, 'IDR': 17045.27,
'INR': 80.5105, 'BRL': 4.0932, 'RUB': 70.6897, 'HRK': 7.442, 'JPY': 130.47, 'THB': 38.66,
'CHF': 1.1739, 'SGD': 1.6274, 'PLN': 4.23, 'BGN': 1.9558, 'TRY': 4.9464, 'CNY': 7.7924,
'NOK': 9.5613, 'NZD': 1.7029, 'ZAR': 14.4937, 'USD': 1.2411, 'MXN': 22.8777, 'ILS': 4.3317,
'GBP': 0.87248, 'KRW': 1336.99, 'MYR': 4.8425}, 'base': 'EUR', 'date': '2018-03-26'}

# Quote against a different currency:
print(api.get_rates('USD'))
{'rates': {'CAD': 1.4352082756, 'HKD': 7.7529324836, 'ISK': 140.2974046366,
'PHP': 51.0298328253, 'DKK': 6.897755611, 'HUF': 327.8562852129, 'CZK': 25.3495889905,
'GBP': 0.8451371571, 'RON': 4.4745543549, 'SEK': 10.1263507897, 'IDR': 16114.9995381916,
'INR': 76.3821926665, 'BRL': 5.0740740741, 'RUB': 78.3240971645, 'HRK': 7.0271543364,
'JPY': 111.4528493581, 'THB': 32.78008682, 'CHF': 0.9792186201, 'EUR': 0.9236168837,
'MYR': 4.3865336658, 'BGN': 1.8064099012, 'TRY': 6.4350235522, 'CNY': 7.0974415812,
'NOK': 10.8751269973, 'NZD': 1.7067516394, 'ZAR': 17.4081463009, 'USD': 1.0,
'MXN': 24.5408700471, 'SGD': 1.4455527847, 'AUD': 1.6618638589, 'ILS': 3.6400665004,
'KRW': 1232.8622887226, 'PLN': 4.2317354761}, 'base': 'USD', 'date': '2020-03-25'}

# Get historical rates for a time period:
print(api.get_rates(start_date="2018-01-01", end_date="2018-01-03"))
{'rates': {'2018-01-03': {'CAD': 1.5047, 'HKD': 9.3985, 'SGD': 1.5988, 'PHP': 59.988,
'DKK': 7.4442, 'HUF': 309.29, 'CZK': 25.545, 'AUD': 1.5339, 'RON': 4.6355, 'SEK': 9.825,
'IDR': 16176.95, 'INR': 76.3455, 'BRL': 3.9236, 'RUB': 69.0962, 'HRK': 7.441, 'JPY': 134.97,
'THB': 39.11, 'CHF': 1.1736, 'PLN': 4.1652, 'BGN': 1.9558, 'TRY': 4.5303, 'CNY': 7.8168,
'NOK': 9.744, 'NZD': 1.6942, 'ZAR': 14.8845, 'USD': 1.2023, 'MXN': 23.3835, 'ILS': 4.1588,
'GBP': 0.8864, 'KRW': 1281.39, 'MYR': 4.8272}, '2018-01-02': {'CAD': 1.5128, 'HKD': 9.4283,
'SGD': 1.6031, 'PHP': 60.132, 'DKK': 7.4437, 'HUF': 308.59, 'CZK': 25.494, 'AUD': 1.5413,
'RON': 4.6525, 'SEK': 9.8283, 'IDR': 16266.03, 'INR': 76.6005, 'BRL': 3.9504, 'RUB': 69.1176,
'HRK': 7.464, 'JPY': 135.35, 'THB': 39.115, 'CHF': 1.1718, 'PLN': 4.1633, 'BGN': 1.9558,
'TRY': 4.534, 'CNY': 7.8338, 'NOK': 9.7748, 'NZD': 1.6955, 'ZAR': 14.9, 'USD': 1.2065,
'MXN': 23.5534, 'ILS': 4.1693, 'GBP': 0.88953, 'KRW': 1281.59, 'MYR': 4.8495}},
'start_at': '2018-01-01', 'base': 'EUR', 'end_at': '2018-01-03'}

# Limit results to specific exchange rates to save bandwidth:
print(api.get_rates(target_list=['ILS', 'JPY'], start_date="2018-01-01",
                    end_date="2018-01-03"))
{'rates': {'2018-01-03': {'JPY': 134.97, 'ILS': 4.1588}, '2018-01-02': {'JPY': 135.35,
'ILS': 4.1693}}, 'start_at': '2018-01-01', 'base': 'EUR', 'end_at': '2018-01-03'}

# Quote the historical rates against a different currency:
print(api.get_rates('USD', start_date="2018-01-01", end_date="2018-01-03"))
{'rates': {'2018-01-03': {'CAD': 1.251517924, 'HKD': 7.8171005573, 'USD': 1.0,
'PHP': 49.8943691258, 'DKK': 6.191632704, 'HUF': 257.2486068369, 'CZK': 21.2467770107,
'GBP': 0.7372535973, 'RON': 3.8555269068, 'SEK': 8.1718373118, 'IDR': 13455.0029110871,
'INR': 63.4995425435, 'BRL': 3.2634117941, 'RUB': 57.470015803, 'HRK': 6.1889711387,
'JPY': 112.2598353156, 'THB': 32.5293188056, 'CHF': 0.9761290859, 'EUR': 0.8317391666,
'MYR': 4.014971305, 'BGN': 1.626715462, 'TRY': 3.7680279464, 'CNY': 6.5015387175,
'NOK': 8.1044664393, 'NZD': 1.409132496, 'ZAR': 12.3800216252, 'MXN': 19.4489728021,
'SGD': 1.3297845796, 'AUD': 1.2758047076, 'ILS': 3.459036846, 'KRW': 1065.7822506862,
'PLN': 3.4643599767}, '2018-01-02': {'CAD': 1.2538748446, 'HKD': 7.8145876502, 'USD': 1.0,
'PHP': 49.8400331538, 'DKK': 6.1696643183, 'HUF': 255.772896809, 'CZK': 21.1305428927,
'GBP': 0.7372813925, 'RON': 3.8561956071, 'SEK': 8.1461251554, 'IDR': 13481.9975134687,
'INR': 63.4898466639, 'BRL': 3.2742644012, 'RUB': 57.2876916701, 'HRK': 6.1864898467,
'JPY': 112.1840033154, 'THB': 32.4202237878, 'CHF': 0.9712391214, 'EUR': 0.828843763,
'MYR': 4.0194778284, 'BGN': 1.6210526316, 'TRY': 3.7579776212, 'CNY': 6.4929962702,
'NOK': 8.1017820141, 'NZD': 1.4053046001, 'ZAR': 12.349772068, 'MXN': 19.5220886863,
'SGD': 1.3287194364, 'AUD': 1.2774968918, 'ILS': 3.4556983009, 'KRW': 1062.23787816,
'PLN': 3.4507252383}}, 'start_at': '2018-01-01', 'base': 'USD', 'end_at': '2018-01-03'}

# Quote the historical rates against for specific currency with custom
# base currency:
print(api.get_rates('USD', ['ILS', 'JPY', 'EUR', 'RUB'],
                    start_date="2018-01-01", end_date="2018-01-03"))
{'rates': {'2018-01-03': {'EUR': 0.8317391666, 'JPY': 112.2598353156, 'RUB': 57.470015803,
'ILS': 3.459036846}, '2018-01-02': {'EUR': 0.828843763, 'JPY': 112.1840033154,
'RUB': 57.2876916701, 'ILS': 3.4556983009}}, 'start_at': '2018-01-01', 'base': 'USD',
'end_at': '2018-01-03'}

# Get the latest foreign exchange rate for EUR and USD:
print(api.get_rate())
1.0827

# Get the latest foreign exchange rate for a specific currency:
print(api.get_rate(target='GBP'))
0.91503

# Get historical rate for any day since 1999:
print(api.get_rate(target='GBP', start_date="2018-03-26"))
0.87248

# Quote against a different currency:
print(api.get_rate('USD', 'GBP'))
0.8451371571

# Get historical rate for a time period:
print(api.get_rate(target='GBP', start_date="2018-01-01",
                   end_date="2018-01-03"))
{'2018-01-03': {'GBP': 0.8864}, '2018-01-02': {'GBP': 0.88953}}

# Quote the historical rates against a different currency:
print(api.get_rate('USD', target='CHF', start_date="2018-01-01",
                   end_date="2018-01-03"))
{'2018-01-03': {'CHF': 0.9761290859}, '2018-01-02': {'CHF': 0.9712391214}}

# Is USD currency supported?
print(api.is_currency_supported('USD'))
True

# Is KKK currency supported?
print(api.is_currency_supported('KKK'))
False

#  Supported currencies list:
print(api.supported_currencies)
['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'AUD', 'RON', 'SEK', 'IDR', 'INR', 'BRL',
'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'SGD', 'PLN', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR',
'USD', 'MXN', 'ILS', 'GBP', 'KRW', 'MYR']
```

# Supported currencies
The list of currencies can be found at [European Central Bank's data set](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html).

If your currency is not in the list, then the library will be of no use to you. You may try [openexchangerates.org API](https://github.com/metglobal/openexchangerates) or some other service.
# License
MIT
