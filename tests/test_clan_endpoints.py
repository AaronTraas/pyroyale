import json
import pytest
import requests_mock
import urllib.parse
import requests

from pyroyale import *
from pyroyale.api import ClanAPI

MOCK_BASEURL = 'mock://test.com'
API_KEY = 'FakeApiKey'
CLAN_TAG = '#FakeClanTag'
CLAN_TAG_ESCAPED = urllib.parse.quote_plus(CLAN_TAG)

api = ClashRoyaleAPI(MOCK_BASEURL, API_KEY, CLAN_TAG)

def test_api_clan_info_success(requests_mock):
    mock_object = {'foo':'bar'}
    mock_url = MOCK_BASEURL + ClanAPI.CLAN_API_ENDPOINT.format(clan_tag=CLAN_TAG_ESCAPED)

    requests_mock.get(mock_url, json=mock_object, status_code=200)

    response_object = api.clan.clan_info()

    assert mock_object == response_object

def test_api_clan_info_failure_clan_tag_not_found(requests_mock):
    mock_url = MOCK_BASEURL + ClanAPI.CLAN_API_ENDPOINT.format(clan_tag=CLAN_TAG_ESCAPED)

    requests_mock.get(mock_url, status_code=404)

    try:
        response_object = api.clan.clan_info()
    except ClashRoyaleAPIClanNotFound as e:
        assert e.clan_tag == CLAN_TAG

def test_api_clan_warlog_success(requests_mock):
    mock_object = { 'items': ['foo', 'bar'] }
    mock_url = MOCK_BASEURL + ClanAPI.WARLOG_API_ENDPOINT.format(clan_tag=CLAN_TAG_ESCAPED)

    requests_mock.get(mock_url, json=mock_object, status_code=200)

    response_object = api.clan.warlog()

    assert mock_object['items'] == response_object

def test_api_clan_warlog_success_noitems(requests_mock):
    mock_object = {'foo':'bar'}
    mock_url = MOCK_BASEURL + ClanAPI.WARLOG_API_ENDPOINT.format(clan_tag=CLAN_TAG_ESCAPED)

    requests_mock.get(mock_url, json=mock_object, status_code=200)

    response_object = api.clan.warlog()

    assert mock_object == response_object

def test_api_api_clan_current_war_success_noitems(requests_mock):
    mock_object = {'foo':'bar'}
    mock_url = MOCK_BASEURL + ClanAPI.CURRENT_WAR_API_ENDPOINT.format(clan_tag=CLAN_TAG_ESCAPED)

    requests_mock.get(mock_url, json=mock_object, status_code=200)

    response_object = api.clan.current_war()

    assert mock_object == response_object
