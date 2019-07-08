import config

api_key, clan_id = config.getConfigData()

def test_credentials():
	assert clan_id == '#JY8YVV'
	assert api_key
