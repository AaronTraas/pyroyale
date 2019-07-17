# coding: utf-8

"""
    Clash Royale API

    Unofficial Swagger definition for the official Clash Royale API  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import sys
import unittest

import pyroyale
from pyroyale.models.war import War  # noqa: E501
from pyroyale.rest import ApiException


class TestWar(unittest.TestCase):
    """War unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDefaults(self):
        model = War()
        pass

    def testConstructorInitializers(self):
        model = War(
            season_id='season_id',
            created_date='created_date',
            participants='participants',
            standings='standings'
        )

        assert model.season_id=='season_id'
        assert model.created_date=='created_date'
        assert model.participants=='participants'
        assert model.standings=='standings'

    def testToDict(self):
        model = War(
            season_id='season_id',
            created_date=123,
            participants={'foo':'bar'},
            standings=[War(season_id='season_id')]
        )

        modelDict = model.to_dict()

        assert modelDict['season_id']=='season_id'
        assert modelDict['participants']['foo']=='bar'
        assert modelDict['created_date']==123
        assert modelDict['standings'][0]['season_id']=='season_id'

    def testToString(self):
        model = War('TestStringSequence')

        modelString = model.to_str()
        assert len(modelString) > 1
        assert 'TestStringSequence' in modelString

    def testPrint(self):
        model = War('TestStringSequence')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(model)
        sys.stdout = sys.__stdout__

        testString = capturedOutput.getvalue()

        assert len(testString) > 1
        assert 'TestStringSequence' in testString


    def testEqual(self):
        model_a  = War('A')
        model_a2 = War('A')
        model_b  = War('B')

        assert model_a == model_a
        assert model_a == model_a2
        assert model_a != model_b
        assert model_a != 'not a'

if __name__ == '__main__':
    unittest.main()
