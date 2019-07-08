import config

import pyroyale
from pyroyale.rest import ApiException

api_key, clan_id = config.getConfigData()

configuration = pyroyale.Configuration()
configuration.api_key['authorization'] = api_key

def test_cards():

    # create an instance of the API class
    api_instance = pyroyale.CardsApi(pyroyale.ApiClient(configuration))

    try:
        # Get list of available cards
        cardList = api_instance.get_cards()
        #print(cardList)
        assert type(cardList.items) == list
        for card in cardList.items:
            if card.id == '26000000':
                assert card.name == 'Knight'
                assert card.max_level == 13
    except ApiException as e:
        print("Exception when calling CardsApi->get_cards: %s\n" % e)
        assert False


