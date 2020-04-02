import pytest


@pytest.fixture
def start_date():
    return '2014-03-26'


@pytest.fixture
def next_date():
    return '2014-03-27'


@pytest.fixture
def end_date():
    return '2014-05-12'


@pytest.fixture
def middle_date():
    return '2014-04-24'


@pytest.fixture
def supported_currencies():
    # for 02.04.2020
    return ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'AUD', 'RON',
            'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF',
            'SGD', 'PLN', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD',
            'MXN', 'ILS', 'GBP', 'KRW', 'MYR']


@pytest.fixture
def targets():
    return ['CAD', 'RUB', 'GBP', 'USD']


@pytest.fixture
def usd():
    return 'USD'


@pytest.fixture
def gbp():
    return 'GBP'


@pytest.fixture
def usd_to_gbp_next_date():
    # rate for USD and GBP on start_date + 1 day (27th)
    return 0.604452179


@pytest.fixture
def usd_to_eur_next_date():
    # rate for EUR and USD on start_date + 1 day (27th)
    return 0.7268498328


@pytest.fixture
def eur_to_gbp_next_date():
    # rate for EUR and GBP on start_date + 1 day (27th)
    return 0.8336
