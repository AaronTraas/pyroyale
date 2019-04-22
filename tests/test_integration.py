from configparser import ConfigParser
import pytest
import os

from pyroyale import *

CLAN_ID = '#JY8YVV'

def getConfigData():
    config_file_name = os.path.expanduser('~/.crtools')

    config = {}

    if not os.path.isfile(config_file_name):
        print('ERROR: ~/.crtools not found.')
        return None

    parser = ConfigParser()
    parser.read(config_file_name)

    # Map the contents of the ini file with the structure for the config object found above.
    for section in parser.sections():
        section_key = section.lower()
        config[section_key] = {}
        for (key, value) in parser.items(section):
            config[section_key][key] = value

    if 'api' not in config:
        print('WARNING: ~/.crtools does not contain section "[api]".')
        return None

    if 'api_key' not in config['api']:
        print('WARNING: ~/.crtools does not contain property "api_key" in section "[api]".')
        return None

    return config['api']['api_key']

api_key = getConfigData()
print('DEBUG: api_key: "{}"'.format(api_key))

api = None
if api_key:
    api = ClashRoyaleAPI(api_key, CLAN_ID)

def test_api_clan_info():
    if not api:
        print('WARNING: skipping integration tests.')
        return

    response = api.clan.clan_info()

    assert response['tag'] == CLAN_ID
    assert response['members'] == len(response['memberList'])

def test_api_clan_warlog():
    if not api:
        print('WARNING: skipping integration tests.')
        return

    response = api.clan.warlog()

    assert len(response) > 0

    in_standings = False
    for clan in response[0]['standings']:
        if clan['clan']['tag'] == CLAN_ID:
            in_standings = True

    assert in_standings == True

def test_api_current_war():
    if not api:
        print('WARNING: skipping integration tests.')
        return

    response = api.clan.current_war()

    assert 'state' in response
    assert response['state'] in ['notInWar', 'collectionDay', 'warDay']

    # if war isn't happening, bail early
    if response['state'] == 'notInWar':
        return

    assert response['clan']['tag'] == CLAN_ID
    assert response['clan']['participants'] == len(response['participants'])
