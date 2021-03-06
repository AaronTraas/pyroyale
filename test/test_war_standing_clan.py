# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger docs for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.war_standing_clan import WarStandingClan  # noqa: E501
from pyroyale.rest import ApiException


class TestWarStandingClan(unittest.TestCase):
    """WarStandingClan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWarStandingClan(self):
        """Test WarStandingClan"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WarStandingClan()  # noqa: E501
        pass

    def testDefaults(self):
        model = WarStandingClan()
        pass

    def testConstructorInitializers(self):
        model = WarStandingClan(
            tag='tag',
            name='name',
            badge_id='badge_id',
            clan_score='clan_score',
            participants='participants',
            battles_played='battles_played',
            crowns = 'crowns',
            wins = 'wins'
        )

        assert model.tag=='tag'
        assert model.name=='name'
        assert model.badge_id=='badge_id'
        assert model.clan_score=='clan_score'
        assert model.participants=='participants'
        assert model.battles_played=='battles_played'
        assert model.crowns=='crowns'
        assert model.wins=='wins'

    def testToDict(self):
        model = WarStandingClan(
            tag={'foo':'bar'},
            clan_score=WarStandingClan(wins=123),
            participants=[WarStandingClan(name='clanname')]
        )

        modelDict = model.to_dict()

        assert modelDict['tag']['foo']=='bar'
        assert modelDict['clan_score']['wins']==123
        assert modelDict['participants'][0]['name']=='clanname'

    def testToString(self):
        model = WarStandingClan('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = WarStandingClan('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = WarStandingClan('A')
        model_a2 = WarStandingClan('A')
        model_b  = WarStandingClan('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'


if __name__ == '__main__':
    unittest.main()
