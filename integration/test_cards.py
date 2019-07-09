import config

import pyroyale
from pyroyale.rest import ApiException

configuration = config.getConfiguration()

def test_cards():

    # create an instance of the API class
    api = pyroyale.CardsApi(pyroyale.ApiClient(configuration))

    try:
        # Get list of available cards
        cardList = api.get_cards()
        #print(cardList)
        assert type(cardList.items) == list
        for card in cardList.items:
            if card.id == '26000000':
                assert card.name == 'Knight'
                assert card.max_level == 13
    except ApiException as e:
        print("Exception when calling CardsApi->get_cards: %s\n" % e)
        assert False


