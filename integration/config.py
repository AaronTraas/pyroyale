import time
from configparser import ConfigParser
import os

import pyroyale

def getConfiguration():
	config_file_name = os.path.expanduser('~/.crtools')

	config = {}

	if not os.path.isfile(config_file_name):
		print('ERROR: ~/.crtools not found.')
		exit(0)

	parser = ConfigParser()
	parser.read(config_file_name)

	# Map the contents of the ini file with the structure for the config object found above.
	for section in parser.sections():
	    section_key = section.lower()
	    config[section_key] = {}
	    for (key, value) in parser.items(section):
	        config[section_key][key] = value

	if 'api' not in config:
		print('ERROR: ~/.crtools does not contain section "[api]".')
		exit(0)

	if 'api_key' not in config['api']:
		print('ERROR: ~/.crtools does not contain property "api_key" in section "[api]".')
		exit(0)

	configuration = pyroyale.Configuration()
	configuration.api_key['authorization'] = config['api']['api_key']

	return configuration
