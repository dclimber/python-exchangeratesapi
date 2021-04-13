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
def old_supported_currencies():
    # for 02.04.2020
    return ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'AUD', 'RON',
            'SEK', 'IDR', 'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF',
            'SGD', 'PLN', 'BGN', 'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'USD',
            'MXN', 'ILS', 'GBP', 'KRW', 'MYR']


@pytest.fixture
def supported_currencies():
    # for 2021-04-13
    return ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG',
            'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND',
            'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD',
            'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC',
            'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN',
            'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP',
            'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF',
            'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD',
            'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD',
            'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL',
            'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO',
            'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
            'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR',
            'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD',
            'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD',
            'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
            'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF',
            'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF',
            'XPF', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL')


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
