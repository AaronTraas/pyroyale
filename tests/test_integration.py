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

    response_object = api.clan.clan_info()

    assert True