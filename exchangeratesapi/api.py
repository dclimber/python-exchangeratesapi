import requests
import os
from datetime import datetime


class ExchangeRatesApiException(Exception):
    """ExchangeRatesApiException"""
    pass


class Api(object):
    API_KEY = os.getenv('EXCHANGERATESAPI_KEY')
    API_TIER = 1
    API_URL = 'https://api.exchangeratesapi.io/v1/{endpoint}{params}'
    endpoints = {
        'latest': 'latest',
        'timeseries': 'timeseries',
        'symbols': 'symbols',
        'convert': 'convert',
        'fluctuation': 'fluctuation',
        'historical': '{date}', #YYYY-MM-DD
    }
    params = {
        'key': 'access_key',
        'base': 'base',
        'symbols': 'symbols',
        'start': 'start_date',
        'end': 'end_date',
        'from': 'from',
        'to': 'to',
        'amount': 'amount',
        'date': 'date',
    }
    DATE_FORMAT = '%Y-%m-%d'
    MIN_YEAR = 1999
    supported_currencies = None

    def __init__(self, api_key=API_KEY):
        """Populate supported currencies list."""
        if not api_key:
            message = ('exchangeratesapi KEY is missing. '
                       'Go to https://manage.exchangeratesapi.io/dashboard')
            raise ExchangeRatesApiException(message)
        self.api_key = api_key
        self.START_PARAM = '?{}={}'.format(self.params['key'], self.api_key)
        self.supported_currencies = self._get_symbols()

    def _get_api_url(self, base, target_list, start_date, end_date):
        """Method to constuct api request url.

        Args:
            param1 (obj): self
            param2 (str): 3-letter currency code
            param3 (list): [(str), (str)]
            param4 (str): date string in format YYYY-mm-dd
            param5 (str): date string in format YYYY-mm-dd

        Returns:
            (str): exchangeratesapi.io url
        """
        endpoint = ''
        params = self.START_PARAM
        if start_date and end_date:
            endpoint = self.endpoints['timeseries']
            params += '&{}={}&{}={}'.format(self.params['start'], start_date,
                                           self.params['end'], end_date)
        elif start_date:
            endpoint = self.endpoints['historical'].format(date=start_date)
        else:
            # latest
            endpoint = self.endpoints['latest']
        if base:
            base_params = '&{}={}'.format(self.params['base'], base)
            params += base_params
        if target_list:
            params += "&{}={}".format(self.params['symbols'],
                                      ",".join(target_list))
        return self.API_URL.format(endpoint=endpoint, params=params)

    def _check_date_format(self, date):
        """Method to check if given date is in correct format
        of %Y-%m-%d (YYYY-mm-dd).

        Returns:
            datetime object or raises ValueError.
        """
        if date:
            return datetime.strptime(date, self.DATE_FORMAT)

    @staticmethod
    def _get_error_message(error):
        """Method to get error message for raising Exception.

        Args:
            param1 (dict): error
            
        Returns:
            (str): error message
        """
        error_message = 'Web Message: {} - {}. '
        error_message += 'https://exchangeratesapi.io/documentation/#errors'
        code = error.get('code', None)
        message = error.get('message', None)
        info = error.get('info', None)
        if message:
            return error_message.format(code, message)
        else:
            return error_message.format(code, info)

    def _get_url(self, url):
        """Method to send a get request to exchangeratesapi,

        Args:
            param1 (obj): self
            param2 (str): url

        Returns:
            (dict): response
            Raise ExchangeRatesApiException if there's bad status code.
        """
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            error = resp.json()['error']
            error_message = self._get_error_message(error)
            raise ExchangeRatesApiException(error_message)

    def _get_symbols(self):
        """Get supported symbols in exchangeratesapi.

        Args:
            param1 (obj): self

        Returns:
            (tuple): supported currencies/symbols
        """
        endpoint = self.endpoints['symbols']
        params = self.START_PARAM
        url = self.API_URL.format(endpoint=endpoint, params=params)
        res = self._get_url(url)
        return tuple(res['symbols'].keys())

    def get_rates(self, base=None, target_list=[],
                  start_date=None, end_date=None):
        """Method to get exchange rates for a given currency
        for a given date.

        Args:
            param1 (obj): self
            param2 (str): 3-letter currency code
            param3 (str): 3-letter currency code
            param4 (str): date string in format YYYY-mm-dd

        Returns:
            (float): currency rate

        Examples:
            ```
            >>> api.get_rates()
            ...
            >>> api.get_rates('USD', ['EUR','CAD','GBP'],
                              start_date="2019-09-12")
            ...
            ```
        """
        self._check_date_format(start_date)
        self._check_date_format(end_date)
        url = self._get_api_url(base, target_list, start_date, end_date)
        return self._get_url(url)
    
    def get_rate(self, base='EUR', target='USD',
                 start_date=None, end_date=None):
        """Method to get exchange rate for a given currency
        for a given date.

        Args:
            param1 (obj): self
            param2 (str): date string in format dd.mm.YYYY
            param3 (str): 3-letter currency code
            param4 (str): 3-letter currency code

        Returns:
            (float): currency rate

        Examples:
            ```
            >>> api.get_rate()
            394.55
            >>> api.get_rate('USD', 'EUR', start_date="2019-09-12")
            0.897
            ```
        """
        res = self.get_rates(base=base, target_list=[target],
                             start_date=start_date, end_date=end_date)
        if end_date:
            return res['rates']
        return res['rates'].get(target)

    def convert(self, amount, base, target, date=None):
        """Method to convert a given amount of a currency
        to another on a given date or latest.

        Args:
            param1 (obj): self
            param2 (int/float): amount
            param3 (str): base
            param4 (str): target
            param5 (str): date

        Returns:
            (float): converted amount

        Examples:
            ```
            >>> api.convert(10, 'EUR', 'USD')
            11.9655
            >>> api.convert(25, 'USD', 'EUR', '2014-03-26')
            18.13265
        """
        if self.API_TIER > 0:
            endpoint = self.endpoints['convert']
            params = self.START_PARAM
            params += '&{}={}&{}={}&{}={}'.format(self.params['from'],
                      base, self.params['to'], target, self.params['amount'],
                      amount)
            if date:
                self._check_date_format(date)
                params+= '&{}={}'.format(self.params['date'], date)
            url = self.API_URL.format(endpoint=endpoint, params=params)
            res = self._get_url(url)
            return res['result']
        else:
            return amount * self.get_rate(base, target, date)

    def fluctuation(self, base, target, start_date=None, end_date=None):
        """Method to get currency's change parameters (margin and percentage),
        optionally between two specified dates.

        Args:
            param1 (obj): self
            param2 (str): base
            param3 (str/list): target
            param4 (str): start_date
            param5 (str): end_date

        Returns:
            (dict): fluctuation
        """
        target_list = target if type(target)==list else [target]
        endpoint = self.endpoints['fluctuation']
        params = self.START_PARAM
        params += '&{}={}&{}={}'.format(self.params['base'], base,
                  self.params['symbols'], ','.join(target_list))
        if start_date:
            if end_date:
                params += '&{}={}&{}={}'.format(self.params['start'],
                          start_date, self.params['end'], end_date)
            else:
                raise ExchangeRatesApiException(
                    "end_date needs to be specified along with start_date.")
        url = self.API_URL.format(endpoint=endpoint, params=params)
        res = self._get_url(url)
        if type(target) == list:
            return res['rates']
        else:
            return res['rates'].get(target)

    def is_currency_supported(self, currency):
        """Method to check if currency is supported.
        
        Args:
            param1 (obj): self
            param2 (str): currency

        Returns:
            (bool): if currency is supported
        """
        return currency in self.supported_currencies
