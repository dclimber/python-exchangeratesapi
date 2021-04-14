import datetime
import os
import pytest
from exchangeratesapi import Api


access_key = os.environ['EXCHANGERATESAPI_FREE_KEY']
api = Api(access_key)


def test_get_api_url_latest(base_url):
    url = api._get_api_url(None, None, None, None)
    assert url == '{}latest?access_key={}'.format(
                    base_url, access_key)


def test_get_api_url_one_latest_targ(base_url, targets):
    url = api._get_api_url(None, targets, None, None)
    assert url == '{}latest?access_key={}&symbols={}'.format(
                    base_url, access_key, ",".join(targets))


def test_get_api_url_one_date(base_url, start_date):
    url = api._get_api_url(None, None, start_date, None)
    assert url == '{}{}?access_key={}'.format(base_url, start_date, access_key)


def test_get_api_url_one_date_targ(base_url, start_date, targets):
    url = api._get_api_url(None, targets, start_date, None)
    assert url == '{}{}?access_key={}&symbols={}'.format(
                    base_url, start_date, access_key, ",".join(targets))


def test_get_api_url_two_dates(base_url, start_date, end_date):
    url = api._get_api_url(None, None, start_date=start_date,
                           end_date=end_date)
    assert url == ('{}timeseries?access_key={}&start_date={}&end_date={}'
                    .format(base_url, access_key, start_date, end_date))


def test_get_api_url_two_dates_targ(base_url, start_date, end_date, targets):
    url = api._get_api_url(None, targets, start_date=start_date,
                           end_date=end_date)
    assert url == ('{}timeseries?access_key={}&start_date={}&end_date={}'
                    '&symbols={}'.format(base_url, access_key, start_date,
                    end_date, ",".join(targets)))


def test_get_api_url_latest_curr(base_url, usd):
    url = api._get_api_url(usd, None, None, None)
    assert url == '{}latest?access_key={}&base={}'.format(
                    base_url, access_key, usd)


def test_get_api_url_one_date_curr(base_url, usd, start_date):
    url = api._get_api_url(usd, None, start_date, None)
    assert url == '{}{}?access_key={}&base={}'.format(
                    base_url, start_date, access_key, usd)


def test_get_api_url_two_dates_curr_targ(base_url, usd, start_date,
                                         end_date, targets):
    url = api._get_api_url(usd, targets, start_date=start_date,
                           end_date=end_date)
    assert url == ('{}timeseries?access_key={}&start_date={}&end_date={}'
                    '&base={}&symbols={}'.format(base_url, access_key,
                    start_date, end_date, usd, ",".join(targets)))


def test_check_date_format(start_date):
    assert type(api._check_date_format(start_date)) == datetime.datetime


def test_check_date_format_fail():
    with pytest.raises(ValueError):
        api._check_date_format("22.02.2012")


def test_get_rates():
    res = api.get_rates()
    assert type(res) == dict
    assert 'rates' in res
    assert 'date' in res
    assert 'base' in res
    assert res['base'] == 'EUR'
    assert type(res['rates']['USD']) == float


def test_get_rates_one_date(start_date):
    res = api.get_rates(start_date=start_date)
    assert type(res) == dict
    assert 'rates' in res
    assert 'base' in res
    assert res['date'] == start_date


def test_get_rates_two_date(start_date, end_date, middle_date):
    res = api.get_rates(start_date=start_date, end_date=end_date)
    assert type(res) == dict
    assert 'rates' in res
    assert 'base' in res
    assert 'start_date' in res
    assert 'end_date' in res
    assert type(res['rates']) == dict
    assert start_date in res['rates']
    assert end_date in res['rates']
    assert middle_date in res['rates']
    assert type(res['rates'][middle_date]['USD']) == float


def test_get_rates_targets(targets):
    res = api.get_rates(target_list=targets)
    curr = targets[0]
    assert set(targets) == set(res['rates'].keys())
    assert type(res['rates'][curr]) == float


def test_get_rates_targets_two_dates(targets, start_date, end_date):
    res = api.get_rates(target_list=targets, start_date=start_date,
                        end_date=end_date)
    assert targets[0] in res['rates'][start_date]
    assert targets[-1] in res['rates'][end_date]


def test_get_rates_curr(usd):
    res = api.get_rates(usd)
    assert res['base'] == usd


def test_get_rates_base_targets_two_dates(usd, start_date, end_date,
                                          usd_to_eur_next_date, next_date):
    res = api.get_rates(usd, start_date=start_date, end_date=end_date)
    assert res['base'] == usd
    assert res['rates'][next_date]['EUR'] == usd_to_eur_next_date


def test_get_rate():
    res = api.get_rate()
    assert type(res) == float


def test_get_rate_targ(gbp):
    res = api.get_rate(target=gbp)
    assert type(res) == float


def test_get_rate_targ_one_date(gbp, next_date, eur_to_gbp_next_date):
    res = api.get_rate(target=gbp, start_date=next_date)
    assert res == eur_to_gbp_next_date  # rate for that date


def test_get_rate_curr_targ_one_date(usd, gbp, start_date,
                                     usd_to_gbp_start_date):
    res = api.get_rate(usd, gbp, start_date)
    assert res == usd_to_gbp_start_date  # rate for that date


def test_get_rate_curr_targ_two_dates(usd, gbp, start_date, end_date,
                                      usd_to_gbp_start_date):
    res = api.get_rate(usd, gbp, start_date, end_date)
    assert res[start_date][gbp] == usd_to_gbp_start_date


def test_supported_currencies(supported_currencies):
    assert api.supported_currencies == supported_currencies


def test_is_currency_supported(usd):
    assert api.is_currency_supported(usd)


def test_is_currency_supported_fail(usd):
    assert not api.is_currency_supported('KKK')
