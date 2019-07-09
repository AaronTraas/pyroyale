import config

import pyroyale
from pyroyale.rest import ApiException

configuration = config.getConfiguration()

def test_clan_agrassar():

    # create an instance of the API class
    api = pyroyale.ClansApi(pyroyale.ApiClient(configuration))

    try:
        clan = api.get_clan('#JY8YVV')
        assert clan.clan_war_trophies > 0
        for member in clan.member_list:
            if member.tag == '#9ULGLRCL':
                assert member.name == 'AaronTraas'


    except ApiException as e:
        print("Exception when calling CardsClan->get_clan: %s\n" % e)
        assert False


