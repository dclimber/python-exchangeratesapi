from exchangeratesapi import Api

api = Api()

print('Get the latest foreign exchange rates:\n', api.get_rates())
print('\nGet historical rates for any day since 1999:\n',
      api.get_rates(start_date="2018-03-26"))
print(
    '\nQuote against a different currency:\n',
    api.get_rates('USD')
)
print(
    '\nGet historical rates for a time period:\n',
    api.get_rates(start_date="2018-01-01", end_date="2018-01-03")
)
print(
    '\nLimit results to specific exchange rates to save bandwidth:\n',
    api.get_rates(target_list=['ILS', 'JPY'], start_date="2018-01-01",
                  end_date="2018-01-03")
)
print(
    '\nQuote the historical rates against a different currency:\n',
    api.get_rates('USD', start_date="2018-01-01", end_date="2018-01-03")
)
print(
    '\nQuote the historical rates against for specific currency with custom '
    'base currency:\n',
    api.get_rates('USD', ['ILS', 'JPY', 'EUR', 'RUB'], start_date="2018-01-01",
                  end_date="2018-01-03")
)
print('Get the latest foreign exchange rate for EUR and USD:\n',
      api.get_rate())
print('Get the latest foreign exchange rate for a specific currency:\n',
      api.get_rate(target='GBP'))
print('\nGet historical rate for any day since 1999:\n',
      api.get_rate(target='GBP', start_date="2018-03-26"))
print(
    '\nQuote against a different currency:\n',
    api.get_rate('USD', 'GBP')
)
print(
    '\nGet historical rate for a time period:\n',
    api.get_rate(target='GBP', start_date="2018-01-01", end_date="2018-01-03")
)
print(
    '\nQuote the historical rates against a different currency:\n',
    api.get_rate('USD', target='CHF', start_date="2018-01-01",
                 end_date="2018-01-03")
)
print(
    '\nIs USD currency supported?', api.is_currency_supported('USD')
)
print(
    '\nIs KKK currency supported?', api.is_currency_supported('KKK')
)
print('\n Supported currencies list:', api.supported_currencies)
