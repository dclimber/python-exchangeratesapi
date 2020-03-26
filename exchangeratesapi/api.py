import requests
from datetime import datetime


class Api(object):
    API_URL = 'https://api.exchangeratesapi.io/{endpoint}{params}'
    endpoints = {
        'latest': 'latest',
        'history': 'history',
    }
    params = {
        'base': 'base',
        'symbols': 'symbols',
        'start': 'start_at',
        'end': 'end_at',
    }
    DATE_FORMAT = '%Y-%m-%d'
    MIN_YEAR = 1999
    supported_currencies = None

    def __init__(self):
        """Populate supported currencies list."""
        rates = self.get_rates()['rates']
        self.supported_currencies = [cur for cur in rates]

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
        params = ''
        if start_date and end_date:
            endpoint = self.endpoints['history']
            params = '?{}={}&{}={}'.format(self.params['start'], start_date,
                                           self.params['end'], end_date)
        elif start_date:
            endpoint = start_date
        else:
            # latest
            endpoint = self.endpoints['latest']
        if base:
            base_params = '{}={}'.format(self.params['base'], base)
            if params != '':
                params += '&'
            else:
                params = '?'
            params += base_params
        if target_list:
            if params != '':
                params += '&'
            else:
                params = '?'
            params += "symbols={}".format(",".join(target_list))
        return self.API_URL.format(endpoint=endpoint, params=params)

    def _check_date_format(self, date):
        """Method to check if given date is in correct format
        of %Y-%m-%d (YYYY-mm-dd).

        Returns:
            datetime object or raises ValueError.
        """
        if date:
            return datetime.strptime(date, self.DATE_FORMAT)

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
            >>> api.get_rate()
            394.55
            >>> api.get_rate('USD', 'EUR', date="2019-09-12")
            0.897
        """
        self._check_date_format(start_date)
        self._check_date_format(end_date)
        url = self._get_api_url(base, target_list, start_date, end_date)
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.json(['error'])

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
            >>> api.get_rate()
            394.55
            >>> api.get_rate('USD', 'EUR', date="2019-09-12")
            0.897
        """
        res = self.get_rates(base=base, target_list=[target],
                             start_date=start_date, end_date=end_date)
        if end_date:
            return res['rates']
        return res['rates'][target]

    def is_currency_supported(self, currency):
        return currency in self.supported_currencies
