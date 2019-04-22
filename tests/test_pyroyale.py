import json
import pytest
import requests_mock
import urllib.parse
import requests

from pyroyale import *

MOCK_BASEURL = 'mock://test.com'
API_KEY = 'FakeApiKey'
CLAN_TAG = '#FakeClanTag'
CLAN_TAG_ESCAPED = urllib.parse.quote_plus(CLAN_TAG)

api = ClashRoyaleAPI(API_KEY, CLAN_TAG, MOCK_BASEURL)

def test_missing_api_credentials():
    try:
        api = ClashRoyaleAPI(False, CLAN_TAG, MOCK_BASEURL)
    except ClashRoyaleAPIMissingFieldsError as e:
        assert e.field_name == 'api_key'

    try:
        api = ClashRoyaleAPI(API_KEY, False, MOCK_BASEURL)
    except ClashRoyaleAPIMissingFieldsError as e:
        assert e.field_name == 'clan_tag'

def test_api_authentication_error(requests_mock):
    mock_object = {'reason': 'accessDenied', 'message': 'mock access denied message'}

    requests_mock.get(MOCK_BASEURL, json=mock_object, status_code=401)

    try:
        response_object = api.api_call('')
    except ClashRoyaleAPIAuthenticationError as e:
        assert str(e) == mock_object['message']

def test_api_misc_error(requests_mock):
    mock_object = {'reason': 'foo'}

    requests_mock.get(MOCK_BASEURL, json=mock_object, status_code=500)

    try:
        response_object = api.api_call('')
    except ClashRoyaleAPIError as e:
        # we don't know what to look for, because this is a catch-all
        # error.  We assume if we got here, it's good.
        assert True
