from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.war_participant import WarParticipant  # noqa: E501
from pyroyale.rest import ApiException


class TestWarParticipant(unittest.TestCase):
    """WarParticipant unit test stubs"""

    def testDefaults(self):
        model = WarParticipant()
        assert True

    def testConstructorInitializers(self):
        model = WarParticipant(
            tag='tag',
            name='name',
            cards_earned='cards_earned',
            battles_played='battles_played',
            collection_day_battles_played='collection_day_battles_played',
            wins='wins'
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.cards_earned=='cards_earned'
        assert model.battles_played=='battles_played'
        assert model.collection_day_battles_played=='collection_day_battles_played'
        assert model.wins=='wins'

    def testToDict(self):
        model = WarParticipant(
            tag={'foo':'bar'},
            battles_played=WarParticipant(name=123),
            collection_day_battles_played=[WarParticipant(name='name')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']['foo']=='bar'
        assert modelDict['battles_played']['name']==123
        assert modelDict['collection_day_battles_played'][0]['name']=='name'

    def testToString(self):
        model = WarParticipant('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = WarParticipant('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = WarParticipant('A')
        model_a2 = WarParticipant('A')
        model_b  = WarParticipant('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
