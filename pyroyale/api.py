#!/usr/bin/python

"""Lightweight wrapper for the Clash Royale API V1 (https://api.clashroyale.com)."""

import logging
import requests
import urllib
import urllib.parse

from .errors import *

class ClashRoyaleAPI:

    baseurl = False
    api_key = False
    clan_tag = False

    def __init__(self, api_key, clan_tag, baseurl='https://api.clashroyale.com'):
        self.logger = logging.getLogger('.'.join([__name__, self.__class__.__name__]))

        if api_key == False:
            raise ClashRoyaleAPIMissingFieldsError('api_key');

        if clan_tag == False:
            raise ClashRoyaleAPIMissingFieldsError('clan_tag');

        self.api_key = api_key
        self.clan_tag = clan_tag
        self.baseurl = baseurl

        self.headers = {
            'Accept': 'application/json',
            'authorization': 'Bearer ' + api_key
        }

        self.clan = ClanAPI(self)

    def api_call(self, endpoint):
        # Make request and handle errors. If request returns a valid object,
        # return that object.
        r = requests.get(self.baseurl + endpoint, headers=self.headers)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 404:
            raise ClashRoyaleAPIClanNotFound(self.clan_tag)
        else:
            reason = 'No reason'
            try:
                reason = r.json()['reason']
            except Exception as e:
                raise ClashRoyaleAPIError("Error connecting to ClashRoyaleAPI ({})".format(r.status_code));

            if(reason == 'accessDenied'):
                raise ClashRoyaleAPIAuthenticationError(r.json()['message'])
            else:
                raise ClashRoyaleAPIError(r.content);


class ClanAPI:

    CLAN_API_ENDPOINT = '/v1/clans/{clan_tag}'
    WARLOG_API_ENDPOINT = '/v1/clans/{clan_tag}/warlog'
    CURRENT_WAR_API_ENDPOINT = '/v1/clans/{clan_tag}/currentwar'

    def __init__(self, api):
        self.api = api
        self.logger = logging.getLogger('.'.join([__name__, self.__class__.__name__]))

    def clan_info(self):
        """Grab clan data from API."""

        self.logger.debug('Retrieving clan data for "{}"'.format(self.api.clan_tag))
        endpoint = self.CLAN_API_ENDPOINT.format(clan_tag=urllib.parse.quote_plus(self.api.clan_tag))
        return self.api.api_call(endpoint)

    def warlog(self):
        """Grab war log data from API."""

        self.logger.debug('Retrieving warlog for "{}"'.format(self.api.clan_tag))
        endpoint = self.WARLOG_API_ENDPOINT.format(clan_tag=urllib.parse.quote_plus(self.api.clan_tag))
        warlog_api = self.api.api_call(endpoint)
        if warlog_api and ('items' in warlog_api):
            return warlog_api['items']
        else:
            return warlog_api

    def current_war(self):
        """Grab war log data from API."""

        self.logger.debug('Retrieving current war data for "{}"'.format(self.api.clan_tag))
        endpoint = self.CURRENT_WAR_API_ENDPOINT.format(clan_tag=urllib.parse.quote_plus(self.api.clan_tag))
        return self.api.api_call(endpoint)
